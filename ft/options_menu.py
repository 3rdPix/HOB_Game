from PyQt6 import QtWidgets, QtCore
from ft.options_menu_signals import OptionsMenuSignals


class OptionsMenuWindow(OptionsMenuSignals):

    def __init__(self, directory: dict, **kwargs) -> None:
        super().__init__(**kwargs)
        self.directory: dict = directory

        self.init_UI()
        self.connect_events()

    def init_UI(self) -> None:
        
        self.fullscreen_checkbox: QtWidgets.QCheckBox = \
            QtWidgets.QCheckBox('Full screen', self)
        
        self.volume_slide: QtWidgets.QSlider = \
            QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self)
        self.volume_slide.setMinimum(0)
        self.volume_slide.setMaximum(100)
        self.volume_slide.setTickInterval(1)
        
        conainter: QtWidgets.QGridLayout = QtWidgets.QGridLayout(self)
        conainter.addWidget(self.fullscreen_checkbox)
        conainter.addWidget(self.volume_slide)
        self.show()
        pass

    def connect_events(self) -> None:
        self.fullscreen_checkbox.toggled.connect(
            self.send_fullscreen_update)
        
        
        pass

    def send_fullscreen_update(self) -> None:
        self.fullscreen_update.emit(self.fullscreen_checkbox.isChecked())
