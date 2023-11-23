import re

class Parser:

    structures: dict = {
    "ghost_variable" : r'^(§|<<)\s@(\w+)$',
    "basic_declaration" : r'^(§|<<)\s(\w+)(>|@)((\(\d+(,\d+)?\))|("[^"]+"))\s#$',
    "multi_level_function" : r'^(§|<<)\s(\w+)\s(-+\w+\s)+(#|##\s(@\w+|\w+))$',
    "variable_by_function" : r'^(§|<<)\s\w+(>|@)((<<|§)\*\*)?\w+\s(-+\w+\s)+(#|##\s@?\w+)$'
    }
    def __init__(self) -> None:
        pass

    def parse(self, input: str) -> dict | None:
        for expression in self.structures.values():
            pattern = re.match(expression, input)
            print(f'pattern: {pattern}')
            return pattern.groups() if pattern else pattern