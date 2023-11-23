import typing
from PyQt6.QtCore import QObject, pyqtSignal


class inGameSignals(QObject):

    logToConsole = pyqtSignal(str, name='log')

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)