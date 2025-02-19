from PyQt6.QtWidgets import QMenuBar
from src.menubar.file_menu import FileMenu
from src.menubar.edit_menu import EditMenu
from src.menubar.format_menu import FormatMenu
from src.menubar.about_menu import AboutMenu


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        # Menu Declarations
        self.file_menu = FileMenu(parent=self)
        self.edit_menu = EditMenu(parent=self)
        self.format_menu = FormatMenu(parent=self)
        self.about_menu = AboutMenu(parent=self)

        # Add menus
        self.addMenu(self.file_menu)
        self.addMenu(self.edit_menu)
        self.addMenu(self.format_menu)
        self.addMenu(self.about_menu)





