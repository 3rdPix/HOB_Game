from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget


class MainMenuSignals(QWidget):

    exit_button_clicked = pyqtSignal(name='exit_button')
    options_button_clicked = pyqtSignal(name='options_button')
    about_button_clicked = pyqtSignal(name='about_button')
    load_button_clicked = pyqtSignal(name='load_button')
    start_button_clicked = pyqtSignal(name='start_button')

    def __init__(self) -> None:
        super().__init__()