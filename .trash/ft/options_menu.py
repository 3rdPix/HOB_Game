from PyQt6 import QtWidgets, QtCore
from ft.options_menu_signals import OptionsMenuSignals


class OptionsMenuWindow(OptionsMenuSignals):

    def __init__(self, directory: dict, **kwargs) -> None:
        super().__init__(**kwargs)
        self.directory: dict = directory

        self.init_UI()

    def init_UI(self) -> None:
        
        self.setMinimumSize(100, 100)

        self.fullscreen_checkbox: QtWidgets.QCheckBox = \
            QtWidgets.QCheckBox('Full screen', self)
        self.fullscreen_checkbox.setEnabled(False)
        

        self.music_enabled_button: QtWidgets.QCheckBox = \
            QtWidgets.QCheckBox('Enable music', self)

        volume_group: QtWidgets.QGroupBox = QtWidgets.QGroupBox('Volume', self)
        self.volume_slide: QtWidgets.QSlider = \
            QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, volume_group)
        self.volume_slide.setMinimum(0)
        self.volume_slide.setMaximum(100)
        self.volume_slide.setTickInterval(1)
        volume_container: QtWidgets.QGridLayout = \
            QtWidgets.QGridLayout(volume_group)
        volume_container.addWidget(self.music_enabled_button)
        volume_container.addWidget(self.volume_slide)

        self.return_button: QtWidgets.QPushButton = \
            QtWidgets.QPushButton('Back', self)
        
        conainter: QtWidgets.QGridLayout = QtWidgets.QGridLayout(self)
        conainter.addWidget(self.fullscreen_checkbox)
        conainter.addWidget(volume_group)
        conainter.addWidget(self.return_button)
        pass

    def enable_slide(self, enabled: bool) -> None:
        self.volume_slide.setEnabled(enabled)