import re

class Parser:

    ghost_variable = r'^(§|<<)\s@\w+$'
    assign_string_number = r'^(§|<<)\s\w+(?:>|@)(\(\d+(,\d+)?\)|"[^"]+") #$'