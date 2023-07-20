from PyQt6 import QtWidgets, QtCore
from ft.new_game_signals import NewGameSignals
from ft.custom_elements import AnimatedButton


class NewGameWindow(NewGameSignals):

    def __init__(self, directory: dict, **kwargs) -> None:
        super().__init__(**kwargs)
        self.directory: dict = directory
        self.init_UI()
        self.connect_events()

    def init_UI(self) -> None:
        upper_container: QtWidgets.QGroupBox = \
            QtWidgets.QGroupBox('Nickname', self)
        self.nickname_box: QtWidgets.QLineEdit = \
            QtWidgets.QLineEdit(self)
        self.nickname_box.setPlaceholderText('Write your hacker name')
        filler: QtWidgets.QGridLayout = QtWidgets.QGridLayout(upper_container)
        filler.addWidget(self.nickname_box)

        self.return_button: QtWidgets.QPushButton = \
            QtWidgets.QPushButton('Go back', self)
        self.loadgame_button: QtWidgets.QPushButton = \
            QtWidgets.QPushButton('Load game', self)
        self.loadgame_button.setEnabled(False)
        self.startgame_button: QtWidgets.QPushButton = \
            QtWidgets.QPushButton('Start game', self)
        
        window_layout: QtWidgets.QGridLayout = QtWidgets.QGridLayout(self)
        window_layout.addWidget(upper_container, 0, 0, 2, 3)
        window_layout.addWidget(self.return_button, 2, 0)
        window_layout.addWidget(self.loadgame_button, 2, 1)
        window_layout.addWidget(self.startgame_button, 2, 2)

    def connect_events(self) -> None:
        self.startgame_button.clicked.connect(
            lambda: self.startgame_with_nick.emit(self.nickname_box.text()))