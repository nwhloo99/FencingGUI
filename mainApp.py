from PyQt5.QtWidgets import QApplication
import sys

from mainWindow import MainWindow

def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    
    win.show()
    sys.exit(app.exec_())
    
window()