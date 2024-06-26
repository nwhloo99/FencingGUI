# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(160, 0, 931, 751))
        self.stackedWidget.setObjectName("stackedWidget")
        self.maskVideoPage = QtWidgets.QWidget()
        self.maskVideoPage.setObjectName("maskVideoPage")
        self.importVideoBar_3 = QtWidgets.QWidget(self.maskVideoPage)
        self.importVideoBar_3.setGeometry(QtCore.QRect(200, 70, 421, 291))
        self.importVideoBar_3.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.importVideoBar_3.setObjectName("importVideoBar_3")
        self.layoutWidget = QtWidgets.QWidget(self.importVideoBar_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 411, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.browse_file_btn_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.browse_file_btn_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browse_file_btn_1.setObjectName("browse_file_btn_1")
        self.horizontalLayout_4.addWidget(self.browse_file_btn_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.perform_masking_btn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perform_masking_btn.sizePolicy().hasHeightForWidth())
        self.perform_masking_btn.setSizePolicy(sizePolicy)
        self.perform_masking_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.perform_masking_btn.setObjectName("perform_masking_btn")
        self.horizontalLayout_5.addWidget(self.perform_masking_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.stackedWidget.addWidget(self.maskVideoPage)
        self.OCRPage = QtWidgets.QWidget()
        self.OCRPage.setObjectName("OCRPage")
        self.OCRButtons = QtWidgets.QWidget(self.OCRPage)
        self.OCRButtons.setGeometry(QtCore.QRect(660, 110, 185, 421))
        self.OCRButtons.setAutoFillBackground(False)
        self.OCRButtons.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.OCRButtons.setObjectName("OCRButtons")
        self.layoutWidget1 = QtWidgets.QWidget(self.OCRButtons)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 20, 121, 381))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.performOCRButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.performOCRButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.performOCRButton.setObjectName("performOCRButton")
        self.verticalLayout.addWidget(self.performOCRButton)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.importVideoBar_2 = QtWidgets.QWidget(self.OCRPage)
        self.importVideoBar_2.setGeometry(QtCore.QRect(30, 120, 511, 371))
        self.importVideoBar_2.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.importVideoBar_2.setObjectName("importVideoBar_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.importVideoBar_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 30, 471, 311))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.browse_file_btn_2 = QtWidgets.QPushButton(self.layoutWidget2)
        self.browse_file_btn_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browse_file_btn_2.setObjectName("browse_file_btn_2")
        self.horizontalLayout_3.addWidget(self.browse_file_btn_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.scoreboard_progress_label = QtWidgets.QLabel(self.layoutWidget2)
        self.scoreboard_progress_label.setObjectName("scoreboard_progress_label")
        self.horizontalLayout_6.addWidget(self.scoreboard_progress_label)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem12)
        self.scoreboardDetection_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.scoreboardDetection_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scoreboardDetection_btn.setObjectName("scoreboardDetection_btn")
        self.verticalLayout_5.addWidget(self.scoreboardDetection_btn)
        self.ocrPageLabel = QtWidgets.QLabel(self.OCRPage)
        self.ocrPageLabel.setGeometry(QtCore.QRect(90, 50, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ocrPageLabel.setFont(font)
        self.ocrPageLabel.setObjectName("ocrPageLabel")
        self.stackedWidget.addWidget(self.OCRPage)
        self.alphaposePage = QtWidgets.QWidget()
        self.alphaposePage.setObjectName("alphaposePage")
        self.alphaposeButtons = QtWidgets.QWidget(self.alphaposePage)
        self.alphaposeButtons.setGeometry(QtCore.QRect(590, 120, 271, 391))
        self.alphaposeButtons.setAutoFillBackground(False)
        self.alphaposeButtons.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.alphaposeButtons.setObjectName("alphaposeButtons")
        self.layoutWidget3 = QtWidgets.QWidget(self.alphaposeButtons)
        self.layoutWidget3.setGeometry(QtCore.QRect(40, 10, 201, 361))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.retrievePoseTrackingDataButton = QtWidgets.QPushButton(self.layoutWidget3)
        self.retrievePoseTrackingDataButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.retrievePoseTrackingDataButton.setObjectName("retrievePoseTrackingDataButton")
        self.verticalLayout_4.addWidget(self.retrievePoseTrackingDataButton)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem14)
        self.retrievePoseTrackingOutput = QtWidgets.QTextEdit(self.layoutWidget3)
        self.retrievePoseTrackingOutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.retrievePoseTrackingOutput.setReadOnly(True)
        self.retrievePoseTrackingOutput.setObjectName("retrievePoseTrackingOutput")
        self.verticalLayout_4.addWidget(self.retrievePoseTrackingOutput)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem15)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.retrievePoseTrackingCommandLine = QtWidgets.QLineEdit(self.layoutWidget3)
        self.retrievePoseTrackingCommandLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.retrievePoseTrackingCommandLine.setObjectName("retrievePoseTrackingCommandLine")
        self.horizontalLayout_9.addWidget(self.retrievePoseTrackingCommandLine)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.retrievePoseTrackingSendButton = QtWidgets.QPushButton(self.layoutWidget3)
        self.retrievePoseTrackingSendButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.retrievePoseTrackingSendButton.setObjectName("retrievePoseTrackingSendButton")
        self.horizontalLayout_9.addWidget(self.retrievePoseTrackingSendButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.importVideoBar = QtWidgets.QWidget(self.alphaposePage)
        self.importVideoBar.setGeometry(QtCore.QRect(30, 120, 491, 311))
        self.importVideoBar.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.importVideoBar.setObjectName("importVideoBar")
        self.layoutWidget4 = QtWidgets.QWidget(self.importVideoBar)
        self.layoutWidget4.setGeometry(QtCore.QRect(40, 20, 431, 261))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem17)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem18)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem19)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.browse_file_btn_3 = QtWidgets.QPushButton(self.layoutWidget4)
        self.browse_file_btn_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browse_file_btn_3.setObjectName("browse_file_btn_3")
        self.horizontalLayout_2.addWidget(self.browse_file_btn_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem20)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem21)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem22)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem23)
        self.performPoseTrackingButton = QtWidgets.QPushButton(self.layoutWidget4)
        self.performPoseTrackingButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.performPoseTrackingButton.setObjectName("performPoseTrackingButton")
        self.verticalLayout_6.addWidget(self.performPoseTrackingButton)
        self.alphaposePageLabel = QtWidgets.QLabel(self.alphaposePage)
        self.alphaposePageLabel.setGeometry(QtCore.QRect(90, 50, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.alphaposePageLabel.setFont(font)
        self.alphaposePageLabel.setWordWrap(True)
        self.alphaposePageLabel.setObjectName("alphaposePageLabel")
        self.stackedWidget.addWidget(self.alphaposePage)
        self.analysisPage = QtWidgets.QWidget()
        self.analysisPage.setObjectName("analysisPage")
        self.widget_3 = QtWidgets.QWidget(self.analysisPage)
        self.widget_3.setGeometry(QtCore.QRect(60, 20, 421, 251))
        self.widget_3.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.analysisPage)
        self.widget_4.setGeometry(QtCore.QRect(60, 270, 421, 41))
        self.widget_4.setStyleSheet("background-color: rgb(24, 24, 24);")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 421, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rewindButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.rewindButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rewindButton.setObjectName("rewindButton")
        self.horizontalLayout.addWidget(self.rewindButton)
        self.playButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.playButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.forwardButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.forwardButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.forwardButton.setObjectName("forwardButton")
        self.horizontalLayout.addWidget(self.forwardButton)
        self.importVideoBar_4 = QtWidgets.QWidget(self.analysisPage)
        self.importVideoBar_4.setGeometry(QtCore.QRect(60, 340, 421, 291))
        self.importVideoBar_4.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.importVideoBar_4.setObjectName("importVideoBar_4")
        self.layoutWidget_2 = QtWidgets.QWidget(self.importVideoBar_4)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 20, 341, 261))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem24)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem25)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem26)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_11.addWidget(self.lineEdit_4)
        self.browse_file_btn_4 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.browse_file_btn_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browse_file_btn_4.setObjectName("browse_file_btn_4")
        self.horizontalLayout_11.addWidget(self.browse_file_btn_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem27)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.isEpeeBtn = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.isEpeeBtn.setAutoExclusive(True)
        self.isEpeeBtn.setObjectName("isEpeeBtn")
        self.horizontalLayout_12.addWidget(self.isEpeeBtn)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem28)
        self.isFoilBtn = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.isFoilBtn.setAutoExclusive(True)
        self.isFoilBtn.setObjectName("isFoilBtn")
        self.horizontalLayout_12.addWidget(self.isFoilBtn)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem29)
        self.isSabreBtn = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.isSabreBtn.setAutoExclusive(True)
        self.isSabreBtn.setObjectName("isSabreBtn")
        self.horizontalLayout_12.addWidget(self.isSabreBtn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem30)
        self.performAnalysisButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.performAnalysisButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.performAnalysisButton.setObjectName("performAnalysisButton")
        self.verticalLayout_7.addWidget(self.performAnalysisButton)
        self.stackedWidget.addWidget(self.analysisPage)
        self.sidebar = QtWidgets.QWidget(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(0, 0, 161, 741))
        self.sidebar.setObjectName("sidebar")
        self.layoutWidget5 = QtWidgets.QWidget(self.sidebar)
        self.layoutWidget5.setGeometry(QtCore.QRect(20, 50, 121, 221))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mask_btn = QtWidgets.QPushButton(self.layoutWidget5)
        self.mask_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mask_btn.setCheckable(True)
        self.mask_btn.setAutoExclusive(True)
        self.mask_btn.setObjectName("mask_btn")
        self.verticalLayout_3.addWidget(self.mask_btn)
        self.ocr_btn = QtWidgets.QPushButton(self.layoutWidget5)
        self.ocr_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ocr_btn.setCheckable(True)
        self.ocr_btn.setAutoExclusive(True)
        self.ocr_btn.setObjectName("ocr_btn")
        self.verticalLayout_3.addWidget(self.ocr_btn)
        self.alphapose_btn = QtWidgets.QPushButton(self.layoutWidget5)
        self.alphapose_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.alphapose_btn.setCheckable(True)
        self.alphapose_btn.setAutoExclusive(True)
        self.alphapose_btn.setObjectName("alphapose_btn")
        self.verticalLayout_3.addWidget(self.alphapose_btn)
        self.analysis_btn = QtWidgets.QPushButton(self.layoutWidget5)
        self.analysis_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.analysis_btn.setCheckable(True)
        self.analysis_btn.setAutoExclusive(True)
        self.analysis_btn.setObjectName("analysis_btn")
        self.verticalLayout_3.addWidget(self.analysis_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_Folder = QtWidgets.QAction(MainWindow)
        self.actionImport_Folder.setObjectName("actionImport_Folder")
        self.menuFile.addAction(self.actionImport_Folder)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Choose video to perform masking"))
        self.label_9.setText(_translate("MainWindow", "File:"))
        self.browse_file_btn_1.setText(_translate("MainWindow", "Browse"))
        self.perform_masking_btn.setText(_translate("MainWindow", "Perform masking"))
        self.label_3.setText(_translate("MainWindow", "When the window opens, select the corners of the scoreboard by clicking. Choose from top left, bottom left, top right, bottom right"))
        self.performOCRButton.setText(_translate("MainWindow", "Perform OCR"))
        self.label_2.setText(_translate("MainWindow", "Detect Scoreboard to obtain boxes.csv and then perform OCR"))
        self.label_6.setText(_translate("MainWindow", "File:"))
        self.browse_file_btn_2.setText(_translate("MainWindow", "Browse"))
        self.scoreboard_progress_label.setText(_translate("MainWindow", "Scoreboard Detection Progress"))
        self.scoreboardDetection_btn.setText(_translate("MainWindow", "Detect Scoreboard"))
        self.ocrPageLabel.setText(_translate("MainWindow", "OCR Processing"))
        self.label_8.setText(_translate("MainWindow", "Retrieve data from alphapose"))
        self.retrievePoseTrackingDataButton.setText(_translate("MainWindow", "Start"))
        self.retrievePoseTrackingSendButton.setText(_translate("MainWindow", "Enter"))
        self.label_10.setText(_translate("MainWindow", "Select masked.mp4"))
        self.label_5.setText(_translate("MainWindow", "File:"))
        self.browse_file_btn_3.setText(_translate("MainWindow", "Browse"))
        self.label_4.setText(_translate("MainWindow", "Alphapose progress"))
        self.performPoseTrackingButton.setText(_translate("MainWindow", "Pose tracking"))
        self.alphaposePageLabel.setText(_translate("MainWindow", "Alphapose Processing"))
        self.rewindButton.setText(_translate("MainWindow", "Rewind"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.forwardButton.setText(_translate("MainWindow", "Forward"))
        self.label_11.setText(_translate("MainWindow", "Select masked.mp4"))
        self.label_7.setText(_translate("MainWindow", "File:"))
        self.browse_file_btn_4.setText(_translate("MainWindow", "Browse"))
        self.isEpeeBtn.setText(_translate("MainWindow", "Epee"))
        self.isFoilBtn.setText(_translate("MainWindow", "Foil"))
        self.isSabreBtn.setText(_translate("MainWindow", "Sabre"))
        self.performAnalysisButton.setText(_translate("MainWindow", "Perform Analysis"))
        self.mask_btn.setText(_translate("MainWindow", "Mask"))
        self.ocr_btn.setText(_translate("MainWindow", "OCR"))
        self.alphapose_btn.setText(_translate("MainWindow", "Alphapose"))
        self.analysis_btn.setText(_translate("MainWindow", "Analysis"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionImport_Folder.setText(_translate("MainWindow", "Import Folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
