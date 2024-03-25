import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os

def checkNumbers(resL, resR, currL, currR, leftCount, rightCount, leftSameCount, rightSameCount, framecount, momentum):
    if (resL[2] > 0.2):
        ## 1 Because score can only increment, 71 because ocr software sometimes detects 1 as 8 when 10 and above
        if (int(resL[1]) == currL):
            leftSameCount += 1
        elif (int(resL[1]) - currL) == 1 or (int(resL[1]) - currL) == 71 or (int(resL[1]) == 37 and currL == 6):
            leftCount += 1

        if (leftCount == 10):
            currL += 1
            netScore = currL - currR
            momentum.append([framecount + 1, netScore])
            leftCount = 0
        elif (leftSameCount == 10):
            leftCount = 0
                
    if (resR[2] > 0.2):
        if (int(resR[1]) == currR):
            rightSameCount += 1
        elif (int(resR[1]) - currR) == 1 or (int(resR[1]) - currR) == 71 or (int(resR[1]) == 37 and currR == 6):
            rightCount += 1

        if (rightCount == 10):
            currR += 1
            netScore = currL - currR
            momentum.append([framecount + 1, netScore])
            rightCount = 0
        elif (rightSameCount == 10):
            rightCount = 0
        
    return currL, currR, leftCount, rightCount, leftSameCount, rightSameCount, momentum


posList = []

def performOcr(folder):
    mycwd = os.getcwd()
    os.chdir(folder)
    global posList
    
    boxes_df = pd.read_csv('./boxes.csv', header=None)
    boxes_df.head()
    cap = cv2.VideoCapture("./masked.mp4")
    framecount = 0
    reader = easyocr.Reader(['en'])
    momentum = [[1, 0]] # Frame number, score
    netScore = 0 # Left positive, Right negative

    # Variables to keep track of number of frames number has changed
    leftCount = 0
    rightCount = 0

    # These two variables are to check if the number should be the same
    leftSameCount = 0
    rightSameCount = 0

    # Variables to keep track of current score
    currL = 0
    currR = 0

    # Variables to ensure that we can capture the scoreboard
    cantFindCount = 0
    found = False
    def onMousePisteCorners(event, x, y, flags, param):
        global posList
        if event == cv2.EVENT_LBUTTONDOWN:
                posList.append([x, y])
                cv2.circle(res, (x,y), radius=10, color=(0,255,0), thickness=-1)
                cv2.imshow('WindowName', res)

    pts2 = [[0,0], [0,360], [540,0], [540,360]]

    while(True):
        ret, frame = cap.read()
        
        if ret == True:

            if not found:
                boxlist = boxes_df.iloc[framecount]
            frame = frame[int(boxlist[1])-20:int(boxlist[3])+20, int(boxlist[0])-20:int(boxlist[2])+20]
            
            res = cv2.resize(frame,None,fx=8, fy=8, interpolation = cv2.INTER_CUBIC)
            if not found:
                cv2.imshow('WindowName', res)
                cv2.setMouseCallback('WindowName', onMousePisteCorners)

                while(1):
                    if cv2.waitKey(10) & 0xFF==ord('q'):
                        cv2.destroyAllWindows()
                        break
                posList = np.float32(posList)
                pts2 = np.float32(pts2)
                found = True

            gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            
            ret, newimage = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)
            frame = newimage
            
            matrix = cv2.getPerspectiveTransform(posList, pts2)
            frame = cv2.warpPerspective(frame, matrix, (540,360))
            h = frame.shape[0]
            w = frame.shape[1]
            
            resL = reader.recognize(frame, [[0, int(w*0.37), int(h*0.57), h]], [], allowlist='0123456789')[0]
            resR = reader.recognize(frame, [[int(w*0.65), w, int(h*0.57), h]], [], allowlist='0123456789')[0]

            frame = cv2.rectangle(frame, (0, int(h*0.57)), (int(w*0.37), h), (0,0,0), 3)
            frame = cv2.rectangle(frame, (int(w*0.65), int(h*0.57)), (w, h), (0,0,0), 3)
            
            currL, currR, leftCount, rightCount, leftSameCount, rightSameCount, momentum = checkNumbers(resL, resR, currL, currR, leftCount, rightCount, leftSameCount, rightSameCount, framecount, momentum)
            
            if (resL[2] > 0.2 and resR[2] > 0.2):
                output = (resL[1], resR[1])
                print(output)
                
            if (resL[2] < 0.1 or resR[2] < 0.1):
                cantFindCount += 1
                if cantFindCount == 30:
                    found = False
                    posList = []
            else:
                cantFindCount = 0
                    
            
            cv2.imshow('frame',frame)
            framecount += 1
            if cv2.waitKey(1) & 0xFF == ord('r'):
                found = False
                posList = []
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    cv2.destroyAllWindows() 
    cap.release()
    
    res = []
    for m in momentum:
        res.append([m[0] / 30, m[1]])
    result = list(zip(*res))
    results_df = pd.DataFrame(res)
    results_df.to_csv('./momentum_results.csv', index=False, header=False)
    
    os.chdir(mycwd)