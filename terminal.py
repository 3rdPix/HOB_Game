import sys
import typing
from PyQt6.QtWidgets import QApplication, QPlainTextEdit, QLineEdit


class Terminal(QApplication):

    def __init__(self, argv: typing.List[str]) -> None:
        super().__init__(argv)

        with open('terminal_style.qss', 'r') as file: style = file.read()

        self.screen = QPlainTextEdit('// HobL terminal\n')
        self.screen.setReadOnly(True)
        self.screen.setMinimumWidth(800)
        self.screen.setMinimumHeight(600)
        self.screen.setObjectName('Screen')
        self.screen.setStyleSheet(style)
        self.screen.move(500, 180)

        self.input = QLineEdit('§ ')
        self.input.setMinimumHeight(60)
        self.input.setMaximumHeight(60)
        self.input.setMinimumWidth(800)
        self.input.setObjectName('Input')
        self.input.setStyleSheet(style)
        self.input.move(500, 800)
        self.input.setFocus()

        self.screen.show()
        self.input.show()


if __name__ == '__main__':

    terminal = Terminal(sys.argv)
    sys.exit(terminal.exec())