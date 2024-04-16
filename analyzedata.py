import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import json
import pandas as pd
import math

def distCalc(pt1, pt2):
    dis = math.sqrt((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2)
    return dis

def calc_dist_from_4m(fencer, pisteLines, leftEngardeToLeftWarning, leftEnGardeToMid, rightEnGardeToMid, rightEngardeToRightWarning):
    # Negative if to the left of engarde, positive otherwise
    if (fencer[0] < pisteLines['leftEngardeLine'][0]):
        # Left side
        distFromLeftEGLine = leftEngardeToLeftWarning * (fencer[0] - pisteLines['leftEngardeLine'][0])
        return distFromLeftEGLine - 200
    elif (fencer[0] < pisteLines['middleLines'][0]):
        distFromMidLine = leftEnGardeToMid * (fencer[0] - pisteLines['middleLines'][0])
        return distFromMidLine
    elif (fencer[0] < pisteLines['rightEngardeLine'][0]):
        distFromMidLine = rightEnGardeToMid * (fencer[0] - pisteLines['middleLines'][0])
        return distFromMidLine
    else:
        distFromRightEGLine = rightEngardeToRightWarning * (fencer[0] - pisteLines['rightEngardeLine'][0])
        return 200 + distFromRightEGLine

## Left fencer score, -200 -> L, -200 - 200 -> M, > 200 -> R
def score_location(dist_chart, time):
    score_dist = dist_chart[time]
    if (score_dist < -200):
        return "SELF_Side"
    elif (-200 <= score_dist and score_dist <= 200):
        return "MID_Side"
    else:
        return "OPP_Side"
    
def did_left_score(prev_momentum, curr_momentum):
    # Momentum calculated by Left - Right
    return (prev_momentum < curr_momentum)

def did_right_score(prev_momentum, curr_momentum):
    # Momentum calculated by Left - Right
    return (prev_momentum > curr_momentum)

## Functions to determine if fencers are at engardeline

def left_at_engarde(dist):
    return (dist < -170) and (dist > -280)

def right_at_engarde(dist):
    return (dist > 170) and (dist < 280)

def fencer_stationary(vel):
    return (vel > -7) and (vel < 7)

def both_fencers_engarde_FE(dist_bw_fencers, left_vel, right_vel):
    return (dist_bw_fencers > 340) and (dist_bw_fencers < 480) and fencer_stationary(left_vel) and fencer_stationary(right_vel)

def both_fencers_engarde(left_dist, right_dist, left_vel, right_vel):
    return left_at_engarde(left_dist) and right_at_engarde(right_dist) and fencer_stationary(left_vel) and fencer_stationary(right_vel)

## Unused
def check_for_start(left_dist_arr, right_dist_arr, left_vel_arr, right_vel_arr, start, end, dist_bw_fencers):
    fencers_engarded = False
    for index in range(start, end):
        left_dist = left_dist_arr[index]
        right_dist = right_dist_arr[index]
        left_vel = left_vel_arr[index]
        right_vel = right_vel_arr[index]
        if not fencers_engarded:
            fencers_engarded = both_fencers_engarde(left_dist, right_dist, left_vel, right_vel)
        else:
            ## Fencers have engarded already, check if they move out towards one another
            if not both_fencers_engarde(left_dist, right_dist, left_vel, right_vel) and left_vel > 0 and right_vel < 0 and dist_bw_fencers[index] < 430:
                return index
    
    return end

def check_for_all_start(left_dist_arr, right_dist_arr, left_vel_arr, right_vel_arr, start, end, dist_bw_fencers):
    fencers_engarded = False
    curr_end = end
    engarde_count = 0
    last_found = 0
    for index in range(start, end):
        left_dist = left_dist_arr[index]
        right_dist = right_dist_arr[index]
        left_vel = left_vel_arr[index]
        right_vel = right_vel_arr[index]
        if not fencers_engarded:
            if both_fencers_engarde(left_dist, right_dist, left_vel, right_vel):
                engarde_count += 1
                last_found = index
            elif (index - last_found > 5):
                engarde_count = 0
            if engarde_count == 5:
                fencers_engarded = True
        else:
            ## Fencers have engarded already, check if they move out towards one another
            if not both_fencers_engarde(left_dist, right_dist, left_vel, right_vel) and left_vel > 0 and right_vel < 0 and dist_bw_fencers[index] < 410:
                curr_end = index
                fencers_engarded = False
                engarde_count = 0
    
    return curr_end

def check_for_all_start_FE(left_dist_arr, right_dist_arr, left_vel_arr, right_vel_arr, start, end, dist_bw_fencers):
    fencers_engarded = False
    curr_end = end
    engarde_count = 0
    last_found = 0
    for index in range(start, end):
        left_dist = left_dist_arr[index]
        right_dist = right_dist_arr[index]
        left_vel = left_vel_arr[index]
        right_vel = right_vel_arr[index]
        if not fencers_engarded:
            if both_fencers_engarde_FE(dist_bw_fencers[index], left_vel, right_vel):
                engarde_count += 1
                last_found = index
            elif (index - last_found > 15):
                engarde_count = 0
            if engarde_count == 30:
                fencers_engarded = True
        else:
            ## Fencers have engarded already, check if they move out towards one another
            if not both_fencers_engarde_FE(dist_bw_fencers[index], left_vel, right_vel) and left_vel > 0 and right_vel < 0:
                curr_end = index
                fencers_engarded = False
                engarde_count = 0
    
    return curr_end

def analyzeData(folder, is_epee=False, is_foil=False):
    mycwd = os.getcwd()
    os.chdir(folder)
    results = pd.read_csv('./momentum_results.csv', header=None)
    os.chdir('./output')
    left_df = pd.read_csv('./left_momentum_results.csv', header=None)
    left_fencer = left_df.to_records(index=False).tolist()

    right_df = pd.read_csv('./right_momentum_results.csv', header=None)
    right_fencer = right_df.to_records(index=False).tolist()
    pisteLines_df = pd.read_csv('./pisteLines.csv')
    pisteLines = {}
    pisteLines['middleLines'] = (pisteLines_df['middleLines'][0], pisteLines_df['middleLines'][1])
    pisteLines['leftEngardeLine'] = (pisteLines_df['leftEngardeLine'][0], pisteLines_df['leftEngardeLine'][1])
    pisteLines['rightEngardeLine'] = (pisteLines_df['rightEngardeLine'][0], pisteLines_df['rightEngardeLine'][1])
    pisteLines['leftWarningLine'] = (pisteLines_df['leftWarningLine'][0], pisteLines_df['leftWarningLine'][1])
    pisteLines['rightWarningLine'] = (pisteLines_df['rightWarningLine'][0], pisteLines_df['rightWarningLine'][1])
    leftEnGardeToMid = 200 / distCalc(pisteLines['middleLines'], pisteLines['leftEngardeLine'])
    rightEnGardeToMid = 200 / distCalc(pisteLines['middleLines'], pisteLines['rightEngardeLine'])
    leftEngardeToLeftWarning = 300 / distCalc(pisteLines['leftEngardeLine'], pisteLines['leftWarningLine'])
    rightEngardeToRightWarning = 300 / distCalc(pisteLines['rightEngardeLine'], pisteLines['rightWarningLine'])

    left_dist = []
    for coord in left_fencer:
        left_dist.append(calc_dist_from_4m(coord, pisteLines, leftEngardeToLeftWarning, leftEnGardeToMid, rightEnGardeToMid, rightEngardeToRightWarning))
        
    right_dist = []
    for coord in right_fencer:
        right_dist.append(calc_dist_from_4m(coord, pisteLines, leftEngardeToLeftWarning, leftEnGardeToMid, rightEnGardeToMid, rightEngardeToRightWarning))
        
    dist_bw_fencers = []
    for i in range(len(left_dist)):
        dist_bw_fencers.append(((right_dist[i] + 700) - (left_dist[i] + 700)))

    vel_left = []
    for i in range(len(left_dist) - 1):
        vel_left.append((left_dist[i + 1] - left_dist[i]))
        
    vel_right = []
    for i in range(len(right_dist) - 1):
        vel_right.append((right_dist[i + 1] - right_dist[i]))
        
    os.chdir('..')
    
    last_time = results[0][0]
    last_momentum = results[1][0]

    results_time = [last_time]
    results_momentum = [last_momentum]

    for i in range(1, len(results[0])):
        time = results[0][i]
        momentum = results[1][i]
        
        if is_epee and (time - last_time) < 5.0:
            # Score should be for both sides
            results_momentum[-1] = momentum
            continue
        elif is_epee and (min(dist_bw_fencers[int(last_time*30) : int(time*30)]) > 400):
            results_momentum[-1] = momentum
        else:
            results_time.append(time)
            results_momentum.append(momentum)
        last_time = time
        last_momentum = momentum
        
    results_time_by_frame = [i * 30 for i in results_time]
    
    minpts = []
    for index in range(1, len(results_time_by_frame)):
        start = int(results_time_by_frame[index - 1])
        end = int(results_time_by_frame[index])
        diff = (end - start)
        last_30 = start + int(diff * 0.7)
        
        hit_time = dist_bw_fencers.index(min(dist_bw_fencers[last_30:end]))
        
        if (did_left_score(results_momentum[index - 1], results_momentum[index])):
            score_loc = score_location(left_dist, hit_time)
            scorer = "Point_Self"
        elif (did_right_score(results_momentum[index - 1], results_momentum[index])):
            score_loc = score_location(right_dist, hit_time)
            scorer = "Point_Opp"
        else:
            score_loc = score_location(right_dist, hit_time)
            scorer = "Simult"
        minpts.append((hit_time, score_loc, scorer))
        
    startpts = []
    for index in range(1, len(results_time_by_frame)):
        start = int(results_time_by_frame[index - 1])
        end = int(results_time_by_frame[index])
        hit = minpts[index-1][0]
        if is_epee or is_foil:
            start_pt = check_for_all_start_FE(left_dist, right_dist, vel_left, vel_right, start, hit, dist_bw_fencers)
        else:
            start_pt = check_for_all_start(left_dist, right_dist, vel_left, vel_right, start, end, dist_bw_fencers)
        startpts.append(start_pt)
        
    minpts_df = pd.DataFrame(minpts)
    minpts_df.to_csv('./ends.csv', index=False, header=False)
    
    startpts_df = pd.DataFrame(startpts)
    startpts_df.to_csv('./start.csv', index=False, header=False)
    
    os.chdir(mycwd)