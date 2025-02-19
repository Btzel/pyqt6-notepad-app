from PyQt6.QtGui import QKeySequence, QAction, QIcon,QTextDocument
from PyQt6.QtWidgets import QMenu,QFileDialog,QMessageBox
from PyQt6.QtCore import QDir,QFileInfo
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog

import sys
ICONS_PATH = "./resources/icons/"

class FileMenu(QMenu):
    def __init__(self,text_edit,parent=None):
        super().__init__("&File",parent)

        # TextEdit reference
        self.text_edit = text_edit

        # New action
        self.new_action = QAction(QIcon(ICONS_PATH+"Add.png"),"New",self)
        self.new_action.setShortcut(QKeySequence("Ctrl+N"))
        self.new_action.setStatusTip("Create a new file")
        self.new_action.triggered.connect(self.new_file)

        # Open action
        self.open_action = QAction(QIcon(ICONS_PATH+"Open.png"),"Open",self)
        self.open_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_action.setStatusTip("Open a new file")
        self.open_action.triggered.connect(self.open_file)

        # Save action
        self.save_action = QAction(QIcon(ICONS_PATH+"Save.png"),"Save",self)
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.save_action.setStatusTip("Save the current file")
        self.save_action.triggered.connect(self.save_file)

        # Print action
        self.print_action = QAction(QIcon(ICONS_PATH+"Print.png"),"Print",self)
        self.print_action.setShortcut(QKeySequence("Ctrl+P"))
        self.print_action.setStatusTip("Print the current document")
        self.print_action.triggered.connect(self.print_file)

        # Print Preview action
        self.print_preview_action = QAction(QIcon(ICONS_PATH+"Preview.png"),"Print Preview",self)
        self.print_preview_action.setShortcut(QKeySequence("Ctrl+Shift+P"))
        self.print_preview_action.setStatusTip("Preview the document before printing")
        self.print_preview_action.triggered.connect(self.print_preview_dialog)

        # Export PDF action
        self.export_pdf_action = QAction(QIcon(ICONS_PATH+"PDF.png"),"Export PDF",self)
        self.export_pdf_action.setShortcut(QKeySequence("Ctrl+E"))
        self.export_pdf_action.setStatusTip("Export the document as PDF")
        self.export_pdf_action.triggered.connect(self.export_pdf)

        # Quit action
        self.quit_action = QAction(QIcon(ICONS_PATH+"Quit.png"),"Quit",self)
        self.quit_action.setShortcut(QKeySequence("Ctrl+Q"))
        self.quit_action.setStatusTip("Exit the application")
        self.quit_action.triggered.connect(self.quit)

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

    def new_file(self):
        if not self.text_edit.document().isModified():
            return

        response = QMessageBox.warning(
            self,
            "Application",
            "Current document has been modified \n"
            "Do you want to save your changes ?",
            QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel
        )

        if response == QMessageBox.StandardButton.Save:
            self.save_file()
            self.text_edit.clear()
        elif response == QMessageBox.StandardButton.Discard:
            self.text_edit.clear()

    def open_file(self):
        if self.text_edit.document().isModified():
            response = QMessageBox.warning(
                self,
                "Application",
                "Current document has been modified \n"
                "Do you want to save your changes ?",
                QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel
            )

            if response == QMessageBox.StandardButton.Save:
                self.save_file()
                self.text_edit.clear()
            elif response == QMessageBox.StandardButton.Discard:
                self.text_edit.clear()


        initial_dir = QDir.homePath() + "/Desktop"
        filename,_ = QFileDialog.getOpenFileName(
            self,
            caption = "Open File",
            directory=initial_dir,
            filter="Text File (*.txt);;Python File(*.py);;"
                   "Markdown File (*.md);;"
                   "HTML File (*.html);;"
                   "Rich Text File (*.rtf);;"
                   "All Files(*)"
        )
        if filename:
            try:
                with open(filename,'r') as file:
                    text = file.read()
                    self.text_edit.setPlainText(text)
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Could not open file: {str(e)}"
                )

    def save_file(self):
        initial_dir = QDir.homePath() + "/Desktop"
        filename,_ = QFileDialog.getSaveFileName(
            self,
            caption="Save File",
            directory=initial_dir,
            filter="Text File (*.txt);;Python File(*.py);;"
                   "Markdown File (*.md);;"
                   "HTML File (*.html);;"
                   "Rich Text File (*.rtf);;"
                   "All Files(*)"
        )
        if filename:
            try:
                with open(filename,'w') as file:
                    text = self.text_edit.toPlainText()
                    file.write(text)
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Could not open file: {str(e)}"
                )

    def print_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.text_edit.print(printer)

    def print_preview_dialog(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        preview_dialog = QPrintPreviewDialog(printer,self)
        preview_dialog.paintRequested.connect(lambda: self.print_preview(printer))
        preview_dialog.exec()

    def print_preview(self,printer):
        self.text_edit.print(printer)

    def export_pdf(self):
        initial_dir = QDir.homePath() + "/Desktop"
        filename, _ = QFileDialog.getSaveFileName(
            caption="Export PDF",
            directory=initial_dir,
            filter ="PDF Files (*.pdf);; All Files (*)"
        )

        if filename:
            if QFileInfo(filename).suffix() == "": filename += '.pdf'
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(filename)
            self.text_edit.document().print(printer)


    @staticmethod
    def quit():
        sys.exit()
