from PyQt6 import QtWidgets, QtCore


class OptionsMenuSignals(QtWidgets.QWidget):

    volume_update = QtCore.pyqtSignal(int, name='volume_change')
    fullscreen_update = QtCore.pyqtSignal(bool, name='fullscreen_change')
    enable_music_udpate = QtCore.pyqtSignal(bool, name='play music or not')

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)