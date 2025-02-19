from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QKeySequence,QAction, QIcon

ICONS_PATH = "./resources/icons/"

class EditMenu(QMenu):
    def __init__(self,parent=None):
        super().__init__("&Edit",parent)
        # Undo action
        self.undo_action = QAction(QIcon(ICONS_PATH+"Undo.png"),"Undo",self)
        self.undo_action.setShortcut(QKeySequence("Ctrl+Z"))
        self.undo_action.setStatusTip("Undo the last operation")

        # Redo action
        self.redo_action = QAction(QIcon(ICONS_PATH+"Redo.png"),"Redo",self)
        self.redo_action.setShortcut(QKeySequence("Ctrl+Y"))
        self.redo_action.setStatusTip("Redo the previously undone operation")

        # Cut action
        self.cut_action = QAction(QIcon(ICONS_PATH+"Cut.png"),"Cut",self)
        self.cut_action.setShortcut(QKeySequence("Ctrl+X"))
        self.cut_action.setStatusTip("Cut the selected text to clipboard")

        # Copy action
        self.copy_action = QAction(QIcon(ICONS_PATH+"Copy.png"),"Copy",self)
        self.copy_action.setShortcut(QKeySequence("Ctrl+C"))
        self.copy_action.setStatusTip("Copy the selected text to clipboard")

        # Paste action
        self.paste_action = QAction(QIcon(ICONS_PATH+"Paste.png"),"Paste",self)
        self.paste_action.setShortcut(QKeySequence("Ctrl+V"))
        self.paste_action.setStatusTip("Paste text from clipboard")

        # Add actions to the edit menu
        self.addAction(self.undo_action)
        self.addAction(self.redo_action)
        self.addSeparator()
        self.addAction(self.cut_action)
        self.addAction(self.copy_action)
        self.addAction(self.paste_action)