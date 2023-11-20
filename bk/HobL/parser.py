import re

class Parser:

    ghost_variable = r'^(§|<<)\s@\w+$'
    assign_string_number = r'^(§|<<)\s\w+(?:>|@)(\(\d+(,\d+)?\)|"[^"]+") #$'
    basic_function = r'^(§|<<)\s\w+\s(-\w+\s)+(#$|##\s(^@\w+|\w+))$'
    multi_level_function = r'^(§|<<)\s\w+\s(-+\w+\s)+(#$|##\s(^@\w+|\w+))$'
    