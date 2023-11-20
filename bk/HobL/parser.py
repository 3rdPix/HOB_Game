import re

class Parser:

    ghost_variable = r'^(§|<<)\s@\w+$'
    basic_declaration = r'^(§|<<)\s\w+(>|@)(\(\d+(,\d+)?\)|"[^"]+")\s#$'
    multi_level_function = r'^(§|<<)\s\w+\s(-+\w+\s)+(#|##\s(@\w+|\w+))$'
    variable_by_function = r'^(§|<<)\s\w+(>|@)((<<|§)\*\*)?\w+\s(-+\w+\s)+(#|##\s@?\w+)$'