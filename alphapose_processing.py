import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import json
import math
import pandas as pd
import sys

# Global variables
pisteLines = {}
pisteLineIdentifiers = ['middleLines', 'leftEngardeLine', 'rightEngardeLine', 'leftWarningLine', 'rightWarningLine', 'leftEndLine', 'rightEndLine']
curr = 0
ptList = []
leftEngardeToLeftWarning = 0
leftEnGardeToMid = 0
rightEnGardeToMid = 0
rightEngardeToRightWarning = 0

def input_ids(frame):
    while True:
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    left_id = int(input('Left Fencer\n'))
    right_id = int(input('Right Fencer\n'))
    skip_frames = int(input('Skip Frames\n'))
    return left_id, right_id, skip_frames

def selectPisteLines():
    cap = cv2.VideoCapture("./output/AlphaPose_masked.mp4")

    ret, frame = cap.read()

    def onMousePisteLines(event, x, y, flags, param):
        global pisteLines
        global pisteLineIdentifiers
        global curr
        global ptList
        if event == cv2.EVENT_LBUTTONDOWN:
            ptList.append((x, y))
        elif event == cv2.EVENT_RBUTTONDOWN:
            print(ptList)
            avg_x = (ptList[0][0] + ptList[1][0]) / 2
            avg_y = (ptList[0][1] + ptList[1][1]) / 2
            pisteLines[pisteLineIdentifiers[curr]] = (avg_x, avg_y)
            curr += 1
            ptList.clear()

    cv2.imshow('Get Piste Lines', frame)
    cv2.setMouseCallback('Get Piste Lines', onMousePisteLines)

    while(1):
        if cv2.waitKey(10) & 0xFF==ord('q'):
            cv2.destroyAllWindows()
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
def check_point_pos_relative_to_line(point, line_pt1, line_pt2):
    v1 = (line_pt2[0]-line_pt1[0], line_pt2[1]-line_pt1[1])   # Vector 1
    v2 = (line_pt2[0]-point[0], line_pt2[1]-point[1])   # Vector 2
    xp = v1[0]*v2[1] - v1[1]*v2[0]  # Cross product (magnitude)
    # If xp > 0, point is above if Xp < 0, point is below else is on the line
    return xp

def average_keypoints(keypoints, confidence_threshold):
    total_considered = 0
    total_y = 0
    total_x = 0
    counter = 0
    kx = 0
    ky = 0
    for count, kp in enumerate(keypoints):
        if (count % 3 == 0):
            kx = kp
        elif (count % 3 == 1):
            ky = kp
        else:
            if kp > confidence_threshold:
                total_considered += 1
                total_y += ky
                total_x += kx
            kx = 0
            ky = 0
    
    average_y = total_y / total_considered
    average_x = total_x / total_considered
    
    return average_x, average_y

def check_point_in_box(point, box_corners):
    # box_corners is an array of points with box coordinates of this order topleft, topright, bottomleft, bottom right
    relative_to_top_line = check_point_pos_relative_to_line(point, box_corners[0], box_corners[1])
    relative_to_bottom_line = check_point_pos_relative_to_line(point, box_corners[2], box_corners[3])
    relative_to_left_line = check_point_pos_relative_to_line(point, box_corners[0], box_corners[2])
    relative_to_right_line = check_point_pos_relative_to_line(point, box_corners[1], box_corners[3])
    return (relative_to_top_line <= 0) and (relative_to_bottom_line >= 0) and (relative_to_left_line >= 0) and (relative_to_right_line <= 0)

# Function to loop through each person detected and render
def loop_through_people_in_piste(keypoints_with_scores, piste_corners):
    personList = []
    for kps in keypoints_with_scores:
        person = kps['keypoints']
        ## x y
        right_ankle = (person[-3], person[-2])
        left_ankle = (person[-6], person[-5])
        right_in = check_point_in_box(right_ankle, piste_corners)
        left_in = check_point_in_box(left_ankle, piste_corners)
        if left_in or right_in:
            personList.append(person)
            
    return personList

def distCalc(pt1, pt2):
    dis = math.sqrt((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2)
    return dis

def calc_dist_from_4m(fencer):
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

def retrieve_alphapose_data(folder):
    os.chdir('./output')

    f = open('alphapose-results.json')

    data = json.load(f)
        
    f.close()

    data_by_frames = []
    curr_frame = 0
    curr_kps = []

    for d in data:
        if (d['image_id'] == (str(curr_frame) + '.jpg') ):
            curr_kps.append(d)
        else:
            
            data_by_frames.append(curr_kps.copy())
            curr_kps.clear()
            curr_kps.append(d)
            curr_frame += 1
    cap = cv2.VideoCapture("AlphaPose_masked.mp4")

    ret, frame = cap.read()

    left_id, right_id, skip_frames = input_ids(frame)

    left_kp = []
    right_kp = []

    frame_count = 0
    for d in data_by_frames[frame_count]:
        if (d['idx'] == left_id):
            left_kp.append(average_keypoints(d['keypoints'], 0.1))
        elif(d['idx'] == right_id):
            right_kp.append(average_keypoints(d['keypoints'], 0.1))
        else:
            pass

    frame_count += 1     
    left_found = False
    right_found = False
    left_no_find_count = 0
    right_no_find_count = 0
    crossed_count = 0
    skip_frames = -1

    while(True):
        ret, frame = cap.read()
        if ret == False:
            break
        # To skip frames, indicate -1, the program will take the last known position of left and right until skip frames is -1 again
        if (skip_frames == -1):
            pass
        else:
            left_kp.append(left_kp[-1])
            right_kp.append(right_kp[-1])
            skip_frames -= 1
            if (skip_frames == 0):
                left_no_find_count = 0
                right_no_find_count = 0
                crossed_count = 0
                left_id, right_id, skip_frames = input_ids(frame)
            frame_count += 1
            continue
            
        try:
            for d in data_by_frames[frame_count]:
                if (d['idx'] == left_id):
                    left_kp.append(average_keypoints(d['keypoints'], 0.1))
                    left_found = True
                    left_no_find_count = 0
                elif(d['idx'] == right_id):
                    right_kp.append(average_keypoints(d['keypoints'], 0.1))
                    right_found = True
                    right_no_find_count = 0
                else:
                    pass
        except IndexError:
            break
            
            
        if not left_found:
            left_kp.append(left_kp[-1])
            left_no_find_count += 1
            if (left_no_find_count == 30):
                left_no_find_count = 0
                right_no_find_count = 0
                crossed_count = 0
                left_id, right_id, skip_frames = input_ids(frame)
                
        
        if not right_found:
            right_kp.append(right_kp[-1])
            right_no_find_count += 1
            if (right_no_find_count == 30):
                left_no_find_count = 0
                right_no_find_count = 0
                crossed_count = 0
                left_id, right_id, skip_frames = input_ids(frame)
                
        if (left_kp[-1][0] > right_kp[-1][0]):
            ## Crossed
            crossed_count += 1
            if (crossed_count == 30):
                left_no_find_count = 0
                right_no_find_count = 0
                crossed_count = 0
                left_id, right_id, skip_frames = input_ids(frame)
                
        left_found = False
        right_found = False
        
        frame_count += 1
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    left_df = pd.DataFrame(left_kp)
    left_df.to_csv('./left_momentum_results.csv', index=False, header=False)
    right_df = pd.DataFrame(right_kp)
    right_df.to_csv('./right_momentum_results.csv', index=False, header=False)
    pisteLines_df = pd.DataFrame(pisteLines)
    pisteLines_df.to_csv('./pisteLines.csv', index=False, header=True)
    
def get_results(folder):
    mycwd = os.getcwd()
    os.chdir(folder)
    selectPisteLines()
    retrieve_alphapose_data(folder)
    os.chdir(mycwd)
    
if __name__ == "__main__":
    folder = sys.argv[1]
    mycwd = os.getcwd()
    os.chdir(folder)
    selectPisteLines()
    retrieve_alphapose_data(folder)
    os.chdir(mycwd)