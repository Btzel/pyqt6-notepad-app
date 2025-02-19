from PyQt6.QtWidgets import QMenu,QMessageBox
from PyQt6.QtGui import QAction,QIcon

ICONS_PATH = "./resources/icons/"

class AboutMenu(QMenu):
    def __init__(self,parent=None):
        super().__init__("&About",parent)
        # About action
        self.about_action = QAction(QIcon(ICONS_PATH+"About.png"),"About App",self)
        self.about_action.setStatusTip("Show information about this application")
        self.about_action.triggered.connect(self.about)
        # Add actions to the about menu
        self.addAction(self.about_action)

    def about(self):
        QMessageBox.about(self,"About App","This is a simple notepad app with PyQt6")