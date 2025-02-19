from main_window import MainWindow
from PyQt6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
screen_size = app.primaryScreen().size()
window = MainWindow(
    screen_width=screen_size.width(),
    screen_height=screen_size.height()
)
window.show()
sys.exit(app.exec())