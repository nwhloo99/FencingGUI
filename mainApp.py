from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QProcess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from pathlib import Path

from ultralytics import YOLO
import sys
import os
import cv2
from matplotlib import pyplot as plt
import pandas as pd
import io
from contextlib import redirect_stdout

from mainAppUI import Ui_MainWindow
from masking import maskVideo
from ocr import performOcr
from posetracking import run_alphapose
from alphapose_processing import get_results

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.alphapose_process = None
        self.alphapose_read_process = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    ## Functions to handle results from QProcesses 
    def alphapose_process_handle_stderr(self):
        data = self.alphapose_process.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.ui.label_4.setText(stderr)
        self.ui.label_4.adjustSize()

    def alphapose_process_handle_stdout(self):
        data = self.alphapose_process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.ui.label_4.setText(stdout)
        self.ui.label_4.adjustSize()

    def alphapose_process_handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        # self.ui.label_4.setText(f"State changed: {state_name}")
        # self.ui.label_4.adjustSize()

    def alphapose_process_finished(self):
        self.ui.label_4.setText("Process finished.")
        self.ui.label_4.adjustSize()
        self.alphapose_process = None
       
    @pyqtSlot() 
    def on_retrieve_alphaposedata_readReady(self):
        cursor = self.ui.retrievePoseTrackingOutput.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(str(self.alphapose_read_process.readAll(), "utf-8"))
        self.ui.retrievePoseTrackingOutput.ensureCursorVisible()
    
    @pyqtSlot()
    def on_retrievePoseTrackingSendButton_clicked(self):
        text = self.ui.retrievePoseTrackingCommandLine.text() + "\n"
        cursor = self.ui.retrievePoseTrackingOutput.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(str(text))
        self.ui.retrievePoseTrackingOutput.ensureCursorVisible()
        self.alphapose_read_process.write(text.encode())
        
    def alphaposedata_process_handle_stdout(self):
        data = self.alphapose_read_process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        cursor = self.ui.retrievePoseTrackingOutput.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(str(stdout))
        
    def alphaposedata_process_finished(self):
        cursor = self.ui.retrievePoseTrackingOutput.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText("Process finished.")
        QApplication.processEvents()
        self.alphapose_read_process = None
        
        
    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.sidebar.findChildren(QPushButton)
        
        for btn in btn_list:
            btn.setAutoExclusive(True)
        
    ## Function for changing menu page     
    def on_mask_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.videoChosen = False
        self.ui.lineEdit.setText("")
    
    ## Function for changing menu page     
    def on_ocr_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.videoChosen = False
        self.ui.lineEdit_2.setText("")
    
    ## Function for changing menu page     
    def on_alphapose_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.videoChosen = False
        self.ui.lineEdit_3.setText("")
    
    ## Function for changing menu page     
    def on_analysis_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    
    @pyqtSlot()
    def on_browse_file_btn_1_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select a File", "C:")
        if filename:
            path = Path(filename)
            self.ui.lineEdit.setText(str(path))
            self.videoChosen = True
            
    @pyqtSlot()
    def on_browse_file_btn_2_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select a File", "C:")
        if filename:
            path = Path(filename)
            self.ui.lineEdit_2.setText(str(path))
            self.videoChosen = True
            
    @pyqtSlot()
    def on_browse_file_btn_3_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select a File", "C:")
        if filename:
            path = Path(filename)
            self.ui.lineEdit_3.setText(str(path))
            self.videoChosen = True
    
    @pyqtSlot()
    def on_performPoseTrackingButton_clicked(self):
        if self.videoChosen:
            path = Path(self.ui.lineEdit_3.text())
            folder = path.parent
            command = run_alphapose(folder, path)
            os.chdir("./AlphaPose")
            self.alphapose_process = QProcess()
            self.alphapose_process.readyReadStandardOutput.connect(self.alphapose_process_handle_stdout)
            self.alphapose_process.readyReadStandardError.connect(self.alphapose_process_handle_stderr)
            self.alphapose_process.stateChanged.connect(self.alphapose_process_handle_state)
            self.alphapose_process.finished.connect(self.alphapose_process_finished)
            self.alphapose_process.start(command)
            os.chdir("..")
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("You have not chosen a video")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            x = msg.exec_()
            
    @pyqtSlot()
    def on_retrievePoseTrackingDataButton_clicked(self):
        if self.videoChosen:
            path = Path(self.ui.lineEdit_3.text())
            folder = path.parent
            self.alphapose_read_process = QProcess()
            self.alphapose_read_process.setProcessChannelMode(QProcess.MergedChannels)
            self.alphapose_read_process.readyRead.connect(self.on_retrieve_alphaposedata_readReady)
            self.alphapose_read_process.readyReadStandardOutput.connect(self.alphaposedata_process_handle_stdout)
            self.alphapose_read_process.finished.connect(self.alphaposedata_process_finished)
            
            self.alphapose_read_process.start("fencingguienv/Scripts/python.exe", ["./alphapose_processing.py", str(folder)])
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("You have not chosen a video")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            x = msg.exec_()
    
    @pyqtSlot()
    def on_scoreboardDetection_btn_clicked(self):
        if self.videoChosen:
            path = Path(self.ui.lineEdit_2.text())
            folder = path.parent
            try:
                model = YOLO('./train17/weights/last.pt')
                mycwd = os.getcwd()
                os.chdir(folder)

                source = "./masked.mp4"
                results = model(source, stream=True)

                boxes = []
                self.ui.scoreboard_progress_label.setText("Started!")
                QApplication.processEvents()
                
                for count, r in enumerate(results):
                    s = "Frame: " + str(count)
                    self.ui.scoreboard_progress_label.setText(s)
                    self.ui.scoreboard_progress_label.adjustSize()
                    QApplication.processEvents()
                    try:
                        boxes.append(r.boxes.xyxy[0].tolist())
                    except:
                        boxes.append(boxes[-1])
                        
                boxes_df = pd.DataFrame(boxes)
                boxes_df = boxes_df.astype('int')
                boxes_df.to_csv('boxes.csv', index=False, header=False)
                
                os.chdir(mycwd)
            except:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error occured")
                msg.setText("Please try again")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                x = msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("You have not chosen a video")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            x = msg.exec_()
            
    @pyqtSlot()
    def on_performOCRButton_clicked(self):
        if self.videoChosen:
            path = Path(self.ui.lineEdit_2.text())
            folder = path.parent
            filename = path.name
            performOcr(folder)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("You have not chosen a video")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            x = msg.exec_()
            
            
    @pyqtSlot()
    def on_perform_masking_btn_clicked(self):
        if self.videoChosen:
            path = Path(self.ui.lineEdit.text())
            folder = path.parent
            filename = path.name
            try:
                maskVideo(folder, filename)
            except:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error occured")
                msg.setText("Please try again")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                x = msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("You have not chosen a video")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            x = msg.exec_()
            
        self.videoChosen = False
        self.ui.lineEdit.setText("")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ## load style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())