import typing
from PyQt6.QtWidgets import QGridLayout, QWidget
from PyQt6.QtCore import pyqtSignal


class QAliveGridLayout(QGridLayout):

    activated: pyqtSignal = pyqtSignal(name='GridLayoutActivated')

    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)

    def activate(self) -> bool:
        my_bool = super().activate()
        self.activated.emit()
        return my_bool