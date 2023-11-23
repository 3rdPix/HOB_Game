import typing
from PyQt6.QtWidgets import QApplication
from ft.game import GameWindow
from ft.main_menu import MainMenuWindow
from bk.instance_handler import InstanceHandler
from bk.inGame import inGame
from ft.options_menu import OptionsMenuWindow
from ft.new_game import NewGameWindow
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
            directory=front_dir.get('options_menu'))
        self.newgame_win: NewGameWindow = NewGameWindow(
            directory=front_dir.get('new_game'))

        self.about_win = 0
        self.loadgame_win = 0
        self.game_win = GameWindow()

        # Create backend handlers
        self.instance_handler: InstanceHandler = InstanceHandler(
            directory=back_dir.get('instance_handler'))
        self.game: inGame = inGame(parent=self)

        # Connect pyqt signals
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
        
        self.instance_handler.hide_main_menu.connect(
            self.main_menu_win.hide)

    def connect_options_instance(self) -> None:
        self.instance_handler.show_options_menu.connect(
            self.options_win.show)
        
        self.options_win.fullscreen_checkbox.toggled.connect(
            self.instance_handler.fullscreen_update)
        
        self.instance_handler.update_instance_volume.connect(
            self.options_win.volume_slide.setValue)
        
        self.options_win.volume_slide.valueChanged.connect(
            self.instance_handler.volume_change)
        
        self.instance_handler.update_fullscreen_status.connect(
            self.options_win.fullscreen_checkbox.setChecked)
        
        self.options_win.return_button.clicked.connect(
            self.instance_handler.return_from_options)
        
        self.instance_handler.show_options_menu.connect(
            self.options_win.show)
        
        self.instance_handler.hide_options_menu.connect(
            self.options_win.hide)
        
        self.options_win.music_enabled_button.toggled.connect(
            self.instance_handler.enable_music)
        
        self.options_win.music_enabled_button.toggled.connect(
            self.options_win.volume_slide.setEnabled)
        
        self.instance_handler.update_music_enabled.connect(
            self.options_win.music_enabled_button.setChecked)
        pass

    def connect_about_instance(self) -> None:
        pass

    def connect_newgame_instance(self) -> None:
        self.main_menu_win.newgame_button.clicked.connect(
            self.newgame_win.show)
        
        self.main_menu_win.newgame_button.clicked.connect(
            self.main_menu_win.hide)
        
        self.newgame_win.return_button.clicked.connect(
            self.newgame_win.hide)
        
        self.newgame_win.return_button.clicked.connect(
            self.main_menu_win.show)
        
        self.newgame_win.startgame_with_nick.connect(
            self.instance_handler.start_from_new)
        
        self.instance_handler.starting_new_game.connect(
            self.newgame_win.hide)
        
        self.instance_handler.starting_new_game.connect(
            self.game_win.show)
        pass

    def connect_loadgame_instance(self) -> None:
        pass

    def connect_game_logic(self) -> None:
        self.game.logToConsole.connect(
            self.game_win.new_line)
        
        self.game_win.sg_ginput.connect(
            self.game.read_ginput)
