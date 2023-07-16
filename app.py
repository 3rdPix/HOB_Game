import typing
from PyQt6.QtWidgets import QApplication
from ft.game import GameWindow
from ft.main_menu import MainMenuWindow
from bk.instance_handler import InstanceHandler
from ft.options_menu import OptionsMenuWindow
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
            back_dir: dict = directory.get('back')

        # Create instances of windows
        self.main_menu_win: MainMenuWindow = MainMenuWindow(
            directory=front_dir.get('main_menu'))
        self.options_win: OptionsMenuWindow = OptionsMenuWindow(
            directory=front_dir.get('options_menu')
        )
        self.about_win = 0
        self.newgame_win = 0
        self.loadgame_win = 0
        self.game_win = GameWindow()

        # Create backend handlers
        self.instance_handler: InstanceHandler = InstanceHandler(
            directory=back_dir.get('instance_handler')
        )
        self.game_logic = 0

        # Connect APIs
        self.connect_mainmenu_instance()
        self.connect_newgame_instance()
        self.connect_loadgame_instance()
        self.connect_options_instance()
        self.connect_about_instance()
        self.connect_game_logic()

        # Holder for work, remove when done
        self.instance_handler.launch()

    def connect_mainmenu_instance(self) -> None:
        self.main_menu_win.exit_button.clicked.connect(
            self.instance_handler.exit_from_main)
        
        self.main_menu_win.about_button.clicked.connect(
            self.instance_handler.open_about_from_main)
        
        self.main_menu_win.options_button.clicked.connect(
            self.instance_handler.open_options_from_main)

        self.main_menu_win.loadgame_button.clicked.connect(
            self.instance_handler.load_game_from_main)

        self.main_menu_win.newgame_button.clicked.connect(
            self.instance_handler.newgame_from_main)

        self.instance_handler.show_main_menu.connect(
            self.main_menu_win.show)
        
        self.instance_handler.update_fullscreen_status.connect(
            self.main_menu_win.full_screen)

    def connect_options_instance(self) -> None:
        self.instance_handler.show_options_menu.connect(
            self.options_win.show)
        
        self.options_win.fullscreen_update.connect(
            self.instance_handler.fullscreen_update)
        
        self.instance_handler.update_instance_volume.connect(
            self.options_win.volume_slide.setValue)
        
        self.options_win.volume_slide.valueChanged.connect(
            self.instance_handler.volume_change)
        
        self.instance_handler.update_fullscreen_status.connect(
            self.options_win.fullscreen_checkbox.setChecked)
        pass

    def connect_about_instance(self) -> None:
        pass

    def connect_newgame_instance(self) -> None:
        pass

    def connect_loadgame_instance(self) -> None:
        pass

    def connect_game_logic(self) -> None:
        pass
