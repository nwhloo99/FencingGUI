from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget, QPushButton, QLabel, QApplication, QMainWindow
from pathlib import Path
import sys

from masking import maskVideo

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.videoChosen = False
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.importVidButton = QPushButton(self.centralwidget)
        self.importVidButton.setObjectName("importVidButton")
        self.importVidButton.clicked.connect(self.selectVideoFile)
        
        self.nextStepButton = QPushButton(self.centralwidget)
        self.nextStepButton.setObjectName("nextStepButton")
        self.nextStepButton.clicked.connect(self.moveToNextStep)
        
        self.label = QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        
        self.filenameEdit = QtWidgets.QLineEdit()
        
        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(QLabel('File:'), 1, 0)
        self.layout.addWidget(self.filenameEdit, 1, 1)
        self.layout.addWidget(self.importVidButton, 1, 2)
        self.layout.addWidget(self.nextStepButton, 2, 0)     
        
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.importVidButton.setText(_translate("MainWindow", "Browse"))
        self.importVidButton.adjustSize()
        self.label.setText(_translate("MainWindow", "Choose which video to analyse"))
        self.label.adjustSize()
        self.nextStepButton.setText(_translate("MainWindow", "Proceed"))
        self.nextStepButton.adjustSize()

    def selectVideoFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select a File", "C:")
        if filename:
            path = Path(filename)
            self.filenameEdit.setText(str(path))
            self.videoChosen = True
            
    def moveToNextStep(self):
        if self.videoChosen:
            path = Path(self.filenameEdit.text())
            folder = path.parent
            filename = path.name
            print(folder)
            print(filename)
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
            