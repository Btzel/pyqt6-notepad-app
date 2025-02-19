from PyQt6.QtWidgets import QToolBar
from PyQt6.QtCore import QSize


class ToolBar(QToolBar):
    def __init__(self,file_menu,edit_menu,format_menu):
        super().__init__()
        # Menu references
        self.file_menu = file_menu
        self.edit_menu = edit_menu
        self.format_menu = format_menu

        # Add menu actions to the toolbar
        self.addAction(self.file_menu.new_action)
        self.addAction(self.file_menu.open_action)
        self.addAction(self.file_menu.save_action)
        self.addSeparator()
        self.addAction(self.file_menu.print_action)
        self.addAction(self.file_menu.export_pdf_action)
        self.addSeparator()
        self.addSeparator()
        self.addSeparator()
        self.addAction(self.edit_menu.undo_action)
        self.addAction(self.edit_menu.redo_action)
        self.addSeparator()
        self.addAction(self.edit_menu.cut_action)
        self.addAction(self.edit_menu.copy_action)
        self.addAction(self.edit_menu.paste_action)
        self.addSeparator()
        self.addSeparator()
        self.addSeparator()
        self.addAction(self.format_menu.bold_action)
        self.addAction(self.format_menu.italic_action)
        self.addAction(self.format_menu.underline_action)
        self.addSeparator()
        self.addAction(self.format_menu.left_action)
        self.addAction(self.format_menu.right_action)
        self.addAction(self.format_menu.center_action)
        self.addAction(self.format_menu.justify_action)