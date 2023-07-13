from PyQt5.QtWidgets import QApplication
from ft.game import GameWindow
from ft.main_menu import MainMenuWindow
from bk.game import GameLogic
import json
import ctypes


class Game(QApplication):

    def __init__(self, argv) -> None:
        super().__init__(argv)

        # holder for windows app recognition -> python host
        myappid = 'hob_game' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
        # Get directory
        with open('paths.json') as paths:
            directory: dict = json.load(paths)
            front_dir: dict = directory.get('front')

        # Create instances of frontend and backend
        self.main_menu_win: MainMenuWindow = MainMenuWindow(
            directory=front_dir.get('main_menu'))
        self.ft_game = GameWindow()
        self.bk_game = GameLogic()

        # Connect APIs
        self.connect_back_to_front()
        self.connect_front_to_back()

        # Holder for work, remove when done
        self.main_menu_win.show()

    def connect_back_to_front(self) -> None:
        pass

    def connect_front_to_back(self) -> None:
        pass