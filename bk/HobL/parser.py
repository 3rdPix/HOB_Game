import re

class NonValidSyntax(Exception):

    def __init__(self) -> None:
        super().__init__('Syntax error')

class Parser:

    #   REGEX ARE NOT WORKING!! :C

    __structures__: dict = {
    "ghost_variable" : r'^(§|<<)\s@(\w+)$',
    "basic_declaration" : r'^(§|<<)\s(\w+)(>|@)(\([+-]?(?:\d*,)?\d+\)|\"[^\"]+\"|\w+)\s(?:(#)$|(##)\s(@?\w+)$)',
    "multi_level_function" : r'^(§|<<)\s(\w+)\s(-+\w+\s)+(#|##\s(@\w+|\w+))$',
    "variable_by_function" : r'^(§|<<)\s\w+(>|@)((<<|§)\*\*)?\w+\s(-+\w+\s)+(#|##\s@?\w+)$'
    }

    @staticmethod
    def parse(input: str) -> dict | None:
        for expression in Parser.__structures__.values():
            pattern = re.match(expression, input)
            if pattern: return pattern.groups()
        raise NonValidSyntax