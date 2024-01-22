import sys
import typing
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QApplication, QPlainTextEdit, QLineEdit
from PyQt6.QtCore import Qt
import re
from bk.HobL.hobl import HobLInterpreter

class InputLine(QLineEdit):

    def stylish(self, style) -> None:
        self.setMinimumHeight(60)
        self.setMaximumHeight(60)
        self.setMinimumWidth(800)
        self.setObjectName('Input')
        self.setStyleSheet(style)
        self.move(500, 800)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setFocus()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Tab:
            self.alternate_start()
            return
        return super().keyPressEvent(event)
        
    def alternate_start(self) -> None:
        if re.match(r'^§ ', self.text()):
            self.setText('<< ' + self.text()[2:])
        elif re.match(r'^(<<) ', self.text()):
            self.setText('// ' + self.text()[3:])
        else:
            self.setText('§ ' + self.text()[3:])

class ConsoleScreen(QPlainTextEdit):

    def stylish(self, style) -> None:
        self.setReadOnly(True)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.setObjectName('Screen')
        self.setStyleSheet(style)
        self.move(500, 180)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)


class Terminal(QApplication):

    def __init__(self, argv: typing.List[str]) -> None:
        super().__init__(argv)

        with open('terminal_style.qss', 'r') as file: style = file.read()

        self.screen = ConsoleScreen('[TERMINAL] Ready')
        self.screen.stylish(style)

        self.input = InputLine('§ ')
        self.input.stylish(style)
        self.input.returnPressed.connect(self.read_input)

        self.interpreter = HobLInterpreter()

        self.screen.show()
        self.input.show()


    def read_input(self) -> None:
        match self.input.text():
            case 'end()': exit()
            case 'clear()': self.screen.setPlainText('[TERMINAL] Ready')
            case _:
                output = self.interpreter.execute_line(self.input.text())
                self.screen.appendPlainText(output.__str__())
        self.input.setText('§ ')

if __name__ == '__main__':

    terminal = Terminal(sys.argv)
    sys.exit(terminal.exec())