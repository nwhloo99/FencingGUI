from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 1200, 600)
        self.setWindowTitle("Fencing CV")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label")
        self.label.move(50,50)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clickb1)
        self.b1.move(300,300)
    
    def clickb1(self):
        self.label.setText("Changed to longer longer text")
        self.update()
        
    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    
    win.show()
    sys.exit(app.exec_())
    
window()