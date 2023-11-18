from abc import ABC
from typing import overload

class HobLVar(ABC):

    @overload
    def __init__(self, name: str, value, type: int) -> None:
        self.__name: str = name
        self.__value = value
        self.__type: int = type

    @overload
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__type: int = 0
        self.__value = None

    

class HobLStr(HobLVar):

    def __init__(self, name: str, value: str=None) -> None:
        if value: super().__init__(name, value, 2)
        else: super().__init__(name)
        

class HobLNum(HobLVar):

    def __init__(self, name: str, value: int=None) -> None:
        if value: super().__init__(name, value, 1)
        else: super().__init__(name)