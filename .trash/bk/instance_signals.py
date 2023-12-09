from PyQt6.QtCore import QObject, pyqtSignal


class InstanceSignals(QObject):

    update_fullscreen_status = pyqtSignal(bool, name='fullscreen_status')
    update_instance_volume = pyqtSignal(int, name='volume from settings to options')
    update_music_enabled = pyqtSignal(bool, name='from setting music enabled')

    show_main_menu = pyqtSignal(name='show_main_menu')
    show_options_menu = pyqtSignal(name='show_options_menu')

    hide_main_menu = pyqtSignal(name='hide_main_menu')
    hide_options_menu = pyqtSignal(name='hide_options_menu')

    starting_new_game = pyqtSignal(name='Start a fresh game with new nickname')

    def __init__(self) -> None:
        super().__init__()