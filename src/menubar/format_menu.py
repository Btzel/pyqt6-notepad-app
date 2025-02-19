from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QKeySequence,QAction, QIcon

ICONS_PATH = "./resources/icons/"

class FormatMenu(QMenu):
    def __init__(self,parent=None):
        super().__init__("&Format",parent)
        # Bold action
        self.bold_action = QAction(QIcon(ICONS_PATH+"Bold.png"),"Bold",self)
        self.bold_action.setShortcut(QKeySequence("Ctrl+B"))
        self.bold_action.setStatusTip("Make the selected text bold")

        # Italic action
        self.italic_action = QAction(QIcon(ICONS_PATH+"Italic.png"),"Italic",self)
        self.italic_action.setShortcut(QKeySequence("Ctrl+I"))
        self.italic_action.setStatusTip("Make the selected text italic")

        # Underline action
        self.underline_action = QAction(QIcon(ICONS_PATH+"Underline.png"),"Underline",self)
        self.underline_action.setShortcut(QKeySequence("Ctrl+U"))
        self.underline_action.setStatusTip("Underline the selected text")

        # Left action
        self.left_action = QAction(QIcon(ICONS_PATH+"Left.png"),"Left",self)
        self.left_action.setShortcut(QKeySequence("Ctrl+L"))
        self.left_action.setStatusTip("Align text to the left")

        # Right action
        self.right_action = QAction(QIcon(ICONS_PATH+"Right.png"),"Right",self)
        self.right_action.setShortcut(QKeySequence("Ctrl+R"))
        self.right_action.setStatusTip("Align text to the right")

        # Center action
        self.center_action = QAction(QIcon(ICONS_PATH+"Center.png"),"Center",self)
        self.center_action.setShortcut(QKeySequence("Ctrl+K"))
        self.center_action.setStatusTip("Center the text")

        # Justify action
        self.justify_action = QAction(QIcon(ICONS_PATH+"Justify.png"),"Justify",self)
        self.justify_action.setShortcut(QKeySequence("Ctrl+J"))
        self.justify_action.setStatusTip("Justify the text")

        # Font action
        self.font_action = QAction(QIcon(ICONS_PATH+"Font.png"),"Font",self)
        self.font_action.setShortcut(QKeySequence("Ctrl+Shift+F"))
        self.font_action.setStatusTip("Change the font settings")

        # Color action
        self.color_action = QAction(QIcon(ICONS_PATH+"Color.png"),"Color",self)
        self.color_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
        self.color_action.setStatusTip("Change the text color")

        # Add actions to the format menu
        self.addAction(self.bold_action)
        self.addAction(self.italic_action)
        self.addAction(self.underline_action)
        self.addSeparator()
        self.addAction(self.left_action)
        self.addAction(self.right_action)
        self.addAction(self.center_action)
        self.addAction(self.justify_action)
        self.addSeparator()
        self.addAction(self.font_action)
        self.addAction(self.color_action)