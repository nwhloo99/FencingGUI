# Fencing GUI
The application helps in the analysis of fencing videos. Currently, it utilizes Ultralytics YOLOv8 to do scoreboard detection followed by easyocr to detect changes in scores. To detect poses, Alphapose is used for pose detection and tracking. The application uses results from both of these areas to make predictions on start and end timings within the fencing bout.

## Setting up

1. pip install -r requirements.txt
2. Import weights for scoreboard detection from https://drive.google.com/drive/folders/11mB6rqxopUEeYFy6dOK3Bu25u4GSc2xu?usp=sharing
3. Import AlphaPose folder from https://drive.google.com/drive/folders/1Y4fODsQtKPwCKQ1Ot1nXeZ7ECROnKFdM?usp=drive_link 
4. Run "python ./AlphaPose/setup.py build develop"