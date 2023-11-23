from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import pyqtSignal


class FronEndSignals(QWidget):

    sg_ginput = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()