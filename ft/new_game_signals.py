from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QWidget


class NewGameSignals(QtWidgets.QWidget):

    startgame_with_nick = QtCore.pyqtSignal(str, name='Start new game under the nick')

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)