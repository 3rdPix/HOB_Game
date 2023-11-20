from PyQt6 import QtMultimedia, QtCore
from bk.instance_signals import InstanceSignals
from os.path import join
import json


class InstanceHandler(InstanceSignals):

    place: int = 0
    player: str

    def __init__(self, directory: dict) -> None:
        super().__init__()
        self.directory: dict = directory

        # Load persisted settings
        with open(join(*directory.get('persisted_settings'))) as data:
            self.game_settings: dict = json.load(data)

        self.init_game_music()
        

    """
    Handler
    """
    def launch(self) -> None:
        self.update_settings()
        self.show_main_menu.emit()
        if self.game_settings.get('music_enabled'): self.music_player.play()

    def init_game_music(self) -> None:
        self.audio_output: QtMultimedia.QAudioOutput = \
            QtMultimedia.QAudioOutput()
        self.audio_output.setVolume(self.game_settings.get('volume'))
        self.music_player: QtMultimedia.QMediaPlayer = \
            QtMultimedia.QMediaPlayer(self)
        self.music_player.setAudioOutput(self.audio_output)
        self.music_player.setLoops(-1)
        self.music_player.setSource(QtCore.QUrl.fromLocalFile(
            join(*self.directory.get('background_song'))))

    def update_settings(self) -> None:
        self.update_fullscreen_status.emit(self.game_settings.get('fullscreen'))
        self.update_instance_volume.emit(int(self.audio_output.volume() * 100))
        self.update_music_enabled.emit(self.game_settings.get('music_enabled'))


    """
    Single-Command emitters
    """
    def fullscreen_update(self, fs: bool) -> None:
        self.game_settings['fullscreen']: bool = fs
        self.update_fullscreen_status.emit(fs)

    """
    API receiver
    """
    def exit_from_main(self) -> None:
        with open(join(*self.directory.get('persisted_settings')), 'w') as file:
            json.dump(self.game_settings, file)
        exit()

    def open_options_from_main(self) -> None:
        self.show_options_menu.emit()
        self.hide_main_menu.emit()
        pass

    def open_about_from_main(self) -> None:
        pass

    def load_game_from_main(self) -> None:
        pass

    def newgame_from_main(self) -> None:
        pass

    def start_from_new(self, nickname: str) -> None:
        # verify if nickname is valid?
        self.player = nickname
        self.place = 2
        self.starting_new_game.emit()
        pass

    def volume_change(self, vol) -> None:
        self.audio_output.setVolume(vol / 100)
        self.game_settings['volume'] = vol / 100

    def enable_music(self, enabled: bool) -> None:
        if not enabled: self.music_player.stop()
        else: self.music_player.play()
        self.game_settings['music_enabled'] = enabled

    def return_from_options(self) -> None:
        match self.place:
            case 0:
                self.show_main_menu.emit()
                self.hide_options_menu.emit()
        pass