from PyQt6.QtWidgets import QMainWindow,QStatusBar,QVBoxLayout,QTextEdit,QHBoxLayout,QWidget
from PyQt6.QtGui import QIcon
from src.menubar.menu_bar import MenuBar
from src.toolbar.tool_bar import ToolBar

class MainWindow(QMainWindow):
    def __init__(self,screen_width,screen_height):
        super().__init__()
        # Main Window Configuration
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.window_width = 1280
        self.window_height = 720
        self.window_pos_x = int((screen_width/2) - (self.window_width/2))
        self.window_pos_y = int((screen_height/2) - (self.window_height/2))
        self.setGeometry(
            self.window_pos_x,
            self.window_pos_y,
            self.window_width,
            self.window_height
        )
        self.setWindowTitle("Notepad")
        self.setWindowIcon(QIcon('./resources/icons/Notepad.png'))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # TextEdit Declaration
        self.text_edit_layout = QHBoxLayout()
        self.text_edit = QTextEdit()
        self.text_edit_layout.addWidget(self.text_edit)
        self.centralWidget.setLayout(self.text_edit_layout)

        # MenuBar Declaration
        self.menu_bar = MenuBar(self.text_edit)
        self.setMenuBar(self.menu_bar)

        # ToolBar Declaration
        self.tool_bar = ToolBar(
            file_menu=self.menu_bar.file_menu,
            edit_menu=self.menu_bar.edit_menu,
            format_menu=self.menu_bar.format_menu
        )
        self.addToolBar(self.tool_bar)

        # StatusBar Declaration
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)


