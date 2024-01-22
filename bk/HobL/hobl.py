from .variables import HobLVariableName, HobLVar
from .parser import Parser, NonValidSyntax


class HobLInterpreter:

    __variables__: dict

    def add_variable(self, name: HobLVariableName, value: HobLVar) -> None:
        self.__variables__['name'] = value

    def delete_variable(self, name: HobLVariableName) -> None:
        value = self.__variables__.get(name)
        del value
        del self.__variables__[name]

    def read_variable(self, name: HobLVariableName) -> HobLVar:
        return self.__variables__.get(name)
    
    def execute_line(self, cmd: str) -> tuple:
        try:
            groups = Parser.parse(cmd)
        except NonValidSyntax as e:
            return e.args,
        return groups
