from ft.game_signals import FronEndSignals
from PyQt6.QtWidgets import QGridLayout, QTextEdit, QLineEdit, QPushButton
from PyQt6 import QtWidgets
from ft.Qt6Custom_widgets import ConsoleScreen


class GameWindow(FronEndSignals):

    def __init__(self) -> None:
        super().__init__()
        self.init_elements()
        self.layout_elements()
        self.connect_events()

    def init_elements(self) -> None:
        # Window
        self.setWindowTitle('Hackers of Blysis')

        # Console
        self.gscreen: ConsoleScreen = ConsoleScreen(parent=self)

        # Input
        self.ginput = QLineEdit()

        # Send button
        self.gsend = QPushButton()

    def layout_elements(self) -> None:
        container = QGridLayout()
        container.addWidget(self.gscreen, 1, 1, 3, 4)
        container.addWidget(self.ginput, 4, 1, 1, 3)
        container.addWidget(self.gsend, 4, 4, 1, 1)
        self.setLayout(container)
        self.ginput.setFocus()

    """
    User-triggered events
    """
    def connect_events(self) -> None:
        self.gsend.clicked.connect(
            self.send_ginput)
        
        self.ginput.returnPressed.connect(
            self.send_ginput)
        
    def send_ginput(self) -> None:
        self.sg_ginput.emit(self.ginput.text())
        self.ginput.clear()
        self.ginput.setFocus()
        
    """
    Back-end commands
    """
    def new_line(self, line: str) -> None:
        self.gscreen.logToConsole(line)