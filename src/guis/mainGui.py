import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import main

class MainGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        #창 제목 설정
        self.setWindowTitle("Last Scavanger")
        #창 크기 설정
        self.setGeometry(100, 100, 600, 800)
        #창 아이콘 설정
        self.setWindowIcon(QIcon("last-scavanger-main-gui-icon.png"))
        #상태 바 설정
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage(main.config.version)

app = QApplication(sys.argv)
win = MainGUI()