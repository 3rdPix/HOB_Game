from bk.inGame_signals import inGameSignals
from .HobL.parser import Parser


class inGame(inGameSignals):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.HobLparser = Parser()

    def read_ginput(self, ginput: str) -> None:
        print(f'ginput: {ginput}')
        get_logs = self.HobLparser.parse(ginput)
        if get_logs:
            self.logToConsole.emit(get_logs.__str__())