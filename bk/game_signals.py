from PyQt5.QtCore import QObject, pyqtSignal


class BackEndSignals(QObject):

    def __init__(self) -> None:
        super().__init__()