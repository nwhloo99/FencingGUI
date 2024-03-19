import cv2
import numpy as np
import os

refPt = []

def maskVideo(folder, filename):
    mycwd = os.getcwd()
    os.chdir(folder)
    cap = cv2.VideoCapture(filename)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    ret, frame = cap.read()
    # refPt = []
    cropping = False

    clone = frame.copy()
    def click_and_crop(event, x, y, flags, param):
        # grab references to the global variables
        global refPt, cropping
        # if the left mouse button was clicked, record the starting
        # (x, y) coordinates and indicate that cropping is being
        # performed
        if event == cv2.EVENT_LBUTTONDOWN:
            refPt = [(x, y)]
            cropping = True
        # check to see if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP:
            # record the ending (x, y) coordinates and indicate that
            # the cropping operation is finished
            refPt.append((x, y))
            cropping = False
            print(refPt)
            # draw a rectangle around the region of interest
            cv2.rectangle(frame, refPt[0], refPt[1], (0, 255, 0), 2)
            cv2.imshow("image", frame)

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", frame)
        key = cv2.waitKey(1) & 0xFF
        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            refPt.clear()
            frame = clone.copy()
        # if the 'c' key is pressed, break from the loop
        elif key == ord("q"):
            break
    
    cv2.destroyAllWindows()
    
    # create a mask
    mask = np.zeros(frame.shape[:2], np.uint8)
    # try:
    mask[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]] = 255
    # except:
    #     os.chdir(mycwd)
    #     out.release()
    #     cap.release()
    #     raise Exception("Crop region not selected properly")

    # Apply mask
    frame = cv2.bitwise_and(frame,frame,mask=mask)

    out = cv2.VideoWriter('masked.mp4',fourcc, 30, (frame_width,frame_height))
    out.write(frame)
            

    while(True):
        ret, frame = cap.read()
    
        if ret == True: 
            # Apply mask
            frame = cv2.bitwise_and(frame,frame,mask=mask)
            
            # Write the frame into the file 'output.avi'
            out.write(frame)
            
            # Display the resulting frame    
            cv2.imshow('frame',frame)

            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print(frame_width)
            break
    

    out.release()
    cap.release()
    
    # Closes all the frames
    cv2.destroyAllWindows()
    
    os.chdir(mycwd)