from PyQt6.QtWidgets import QMenu, QFontDialog, QColorDialog
from PyQt6.QtGui import QKeySequence,QAction, QIcon,QFont
from PyQt6.QtCore import Qt

ICONS_PATH = "./resources/icons/"

class FormatMenu(QMenu):
    def __init__(self,text_edit,parent=None):
        super().__init__("&Format",parent)
        self.font = QFont()
        self.color = None
        # TextEdit reference
        self.text_edit = text_edit
        # Bold action
        self.bold_action = QAction(QIcon(ICONS_PATH+"Bold.png"),"Bold",self)
        self.bold_action.setShortcut(QKeySequence("Ctrl+B"))
        self.bold_action.setStatusTip("Make the selected text bold")
        self.bold_action.triggered.connect(self.bold_text)

        # Italic action
        self.italic_action = QAction(QIcon(ICONS_PATH+"Italic.png"),"Italic",self)
        self.italic_action.setShortcut(QKeySequence("Ctrl+I"))
        self.italic_action.setStatusTip("Make the selected text italic")
        self.italic_action.triggered.connect(self.italic_text)

        # Underline action
        self.underline_action = QAction(QIcon(ICONS_PATH+"Underline.png"),"Underline",self)
        self.underline_action.setShortcut(QKeySequence("Ctrl+U"))
        self.underline_action.setStatusTip("Underline the selected text")
        self.underline_action.triggered.connect(self.underline_text)

        # Left action
        self.left_action = QAction(QIcon(ICONS_PATH+"Left.png"),"Left",self)
        self.left_action.setShortcut(QKeySequence("Ctrl+L"))
        self.left_action.setStatusTip("Align text to the left")
        self.left_action.triggered.connect(self.align_left)

        # Right action
        self.right_action = QAction(QIcon(ICONS_PATH+"Right.png"),"Right",self)
        self.right_action.setShortcut(QKeySequence("Ctrl+R"))
        self.right_action.setStatusTip("Align text to the right")
        self.right_action.triggered.connect(self.align_right)

        # Center action
        self.center_action = QAction(QIcon(ICONS_PATH+"Center.png"),"Center",self)
        self.center_action.setShortcut(QKeySequence("Ctrl+K"))
        self.center_action.setStatusTip("Center the text")
        self.center_action.triggered.connect(self.align_center)

        # Justify action
        self.justify_action = QAction(QIcon(ICONS_PATH+"Justify.png"),"Justify",self)
        self.justify_action.setShortcut(QKeySequence("Ctrl+J"))
        self.justify_action.setStatusTip("Justify the text")
        self.justify_action.triggered.connect(self.align_justify)

        # Font action
        self.font_action = QAction(QIcon(ICONS_PATH+"Font.png"),"Font",self)
        self.font_action.setShortcut(QKeySequence("Ctrl+Shift+F"))
        self.font_action.setStatusTip("Change the font settings")
        self.font_action.triggered.connect(self.text_font)

        # Color action
        self.color_action = QAction(QIcon(ICONS_PATH+"Color.png"),"Color",self)
        self.color_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
        self.color_action.setStatusTip("Change the text color")
        self.color_action.triggered.connect(self.text_color)

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

    def bold_text(self):
        cursor = self.text_edit.textCursor()
        text_format = cursor.charFormat()
        is_bold = text_format.font().bold()
        self.font.setBold(not is_bold)
        text_format.setFont(self.font)
        self.text_edit.mergeCurrentCharFormat(text_format)

    def italic_text(self):
        cursor = self.text_edit.textCursor()
        text_format = cursor.charFormat()
        is_italic = text_format.font().italic()
        self.font.setItalic(not is_italic)
        text_format.setFont(self.font)
        self.text_edit.mergeCurrentCharFormat(text_format)

    def underline_text(self):
        cursor = self.text_edit.textCursor()
        text_format = cursor.charFormat()
        is_underline = text_format.font().underline()
        self.font.setUnderline(not is_underline)
        text_format.setFont(self.font)
        self.text_edit.mergeCurrentCharFormat(text_format)

    def align_left(self):
        self.text_edit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def align_right(self):
        self.text_edit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def align_center(self):
        self.text_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def align_justify(self):
        self.text_edit.setAlignment(Qt.AlignmentFlag.AlignJustify)

    def text_font(self):
        font,ok = QFontDialog.getFont()
        self.font = font
        if ok:
            self.text_edit.setFont(self.font)

    def text_color(self):
        color = QColorDialog.getColor()
        if color:
            self.text_edit.setTextColor(color)


