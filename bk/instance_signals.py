from PyQt6.QtCore import QObject, pyqtSignal


class InstanceSignals(QObject):

    update_fullscreen_status = pyqtSignal(bool, name='fullscreen_status')
    update_instance_volume = pyqtSignal(int, name='volume from settings to options')

    show_main_menu = pyqtSignal(name='show_main_menu')
    show_options_menu = pyqtSignal(name='show_options_menu')

    def __init__(self) -> None:
        super().__init__()