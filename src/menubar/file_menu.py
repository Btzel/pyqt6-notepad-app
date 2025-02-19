from PyQt6.QtGui import QKeySequence, QAction, QIcon
from PyQt6.QtWidgets import QMenu

ICONS_PATH = "./resources/icons/"

class FileMenu(QMenu):
    def __init__(self,parent=None):
        super().__init__("&File",parent)
        # New action
        self.new_action = QAction(QIcon(ICONS_PATH+"Add.png"),"New",self)
        self.new_action.setShortcut(QKeySequence("Ctrl+N"))
        self.new_action.setStatusTip("Create a new file")

        # Open action
        self.open_action = QAction(QIcon(ICONS_PATH+"Open.png"),"Open",self)
        self.open_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_action.setStatusTip("Open a new file")

        # Save action
        self.save_action = QAction(QIcon(ICONS_PATH+"Save.png"),"Save",self)
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.save_action.setStatusTip("Save the current file")

        # Print action
        self.print_action = QAction(QIcon(ICONS_PATH+"Print.png"),"Print",self)
        self.print_action.setShortcut(QKeySequence("Ctrl+P"))
        self.print_action.setStatusTip("Print the current document")

        # Print Preview action
        self.print_preview_action = QAction(QIcon(ICONS_PATH+"Preview.png"),"Print Preview",self)
        self.print_preview_action.setShortcut(QKeySequence("Ctrl+Shift+P"))
        self.print_preview_action.setStatusTip("Preview the document before printing")

        # Export PDF action
        self.export_pdf_action = QAction(QIcon(ICONS_PATH+"PDF.png"),"Export PDF",self)
        self.export_pdf_action.setShortcut(QKeySequence("Ctrl+E"))
        self.export_pdf_action.setStatusTip("Export the document as PDF")

        # Quit action
        self.quit_action = QAction(QIcon(ICONS_PATH+"Quit.png"),"Quit",self)
        self.quit_action.setShortcut(QKeySequence("Ctrl+Q"))
        self.quit_action.setStatusTip("Exit the application")

        # Add actions to the file menu
        self.addAction(self.new_action)
        self.addAction(self.open_action)
        self.addAction(self.save_action)
        self.addSeparator()
        self.addAction(self.print_action)
        self.addAction(self.print_preview_action)
        self.addAction(self.export_pdf_action)
        self.addSeparator()
        self.addAction(self.quit_action)