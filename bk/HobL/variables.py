import abc
from _collections_abc import _check_methods
import re
from typing import Protocol
import sys
from PyQt6.QtCore import pyqtSignal

"""
Protocol definitions
"""

class NonValidHobLName(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NameLike(abc.ABC):
    """Abstract base class for implementing the name-like protocol."""

    @abc.abstractmethod
    def __namestr__(self):
        """Return the name string representation of the object."""
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is NameLike:
            return _check_methods(subclass, '__namestr__')
        return NotImplemented
    

class HobLVariableName(NameLike):

    def __init__(self, name):
        if not re.match(r'\w+', name):
            raise NonValidHobLName(
                f"Value does not match NameLike pattern: {name}")
        self._name = name

    def __namestr__(self):
        return self._name


class NumberLike(abc.ABC):
    """Abstract base class for implementing the number-like protocol."""

    @abc.abstractmethod
    def __numstr__(self):
        """Return the numeric string representation of the object."""
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is NumberLike:
            return _check_methods(subclass, '__numstr__')
        return NotImplemented


class HobLNumber(NumberLike):
    def __init__(self, value):
        if isinstance(value, (int, float)): self.value = value
        elif isinstance(value, str):
            # Replace comma with dot for decimal separation
            value = value.replace(',', '.')
            if re.match(r'^-?\d+(\.\d+)?$', value):
                # Convert string to int or float if it represents a number
                self.value = float(value) if '.' in value else int(value)
            else:
                raise ValueError(
                    f"The value '{value}' is not a valid HobLNumber.")
        else:
            raise ValueError(f"The value '{value}' is not a valid HobLNumber.")

    def __numstr__(self):
        return str(self.value)

"""
Variable types
"""

class HobLGhostAny:

    def __init__(self, name: HobLVariableName) -> None:
        self.name = name


class HobLGhostEvent:

    def __init__(self, name: HobLVariableName) -> None:
        self.name = name


def expect_event(ghostVar: HobLGhostAny) -> HobLGhostEvent:
    """Turns an unkwown variable type to a ghost event"""
    new = HobLGhostEvent(ghostVar.name)
    del ghostVar
    return new

# Maybe pass the values as properties and use signals inside setter?
# Will do!! But only for OOP
class HobLVar(abc.ABC):

    """General description of any variable"""

    alterEvent:     pyqtSignal = pyqtSignal(name='alterEvent')
    deletionEvent:  pyqtSignal = pyqtSignal(name='deletionEvent')
    syncrodEvent:   pyqtSignal = pyqtSignal(name='syncrodEvent')
    dsynrcodEvent:  pyqtSignal = pyqtSignal(name='dsyncrodEvent')
    name: HobLVariableName

    def syncro(self) -> None: self.syncrodEvent.emit()
    def dsyncrod(self) -> None: self.dsynrcodEvent.emit()


class HobLNumberVariableStructure(HobLVar):

    increaseEvent: pyqtSignal = pyqtSignal(name='increaseEvent')
    decreaseEvent: pyqtSignal = pyqtSignal(name='decreaseEvent')


class HobLNumberVariable(HobLNumberVariableStructure):

    def __init__(self, name: HobLVariableName,
                 value: HobLNumber) -> None:
        super().__init__()
        self.name = name
        self.value = value

    def __modify(self, new_value: HobLNumber) -> None:
        """This method should only be called from OOP of this variable"""
        if not new_value != self.value: return
        self.alterEvent.emit()
        if new_value > self.value: self.increaseEvent.emit()
        elif new_value < self.value: self.decreaseEvent.emit()
        self.value = new_value


class HobLNumberOOP(HobLNumberVariableStructure):

    def __init__(self, origin: HobLNumberVariable,
                 name: HobLVariableName) -> None:
        self.origin = origin
        self.name = name
        self.setHobLProperties()

    def setHobLProperties(self) -> None:
        self._value = self.origin.value
        self.size = sys.getsizeof(self)

    def get_value(self) -> HobLNumber: return self._value
    def set_value(self, new_value: HobLNumber) -> None:
        if not new_value != self.value: return
        self.alterEvent.emit()
        if new_value > self.value: self.increaseEvent.emit()
        elif new_value < self.value: self.decreaseEvent.emit()
        self._value = new_value

    value = property(get_value, set_value)

    def increase(self) -> None: self.value += 1
    def decrease(self) -> None: self.value -= 1
    def square(self) -> None: self.value *= self.value
    def half(self) -> None: self.value /= 2

    def do(self) -> None:
        raise NotImplementedError


class HobLStringVariableStructure(HobLVar):

    verboseEvent:   pyqtSignal = pyqtSignal(name='verboseEvent')
    dverboseEvent:  pyqtSignal = pyqtSignal(name='dverboseEvent')
    weightedEvent:  pyqtSignal = pyqtSignal(name='weightedEvent')
    dweightedEvent: pyqtSignal = pyqtSignal(name='dweightedEvent')
    

class HobLStringVariable(HobLStringVariableStructure):

    def __init__(self, name: HobLVariableName, value: str) -> None:
        super().__init__()
        self.name = name
        self.value = value
        self.length = len(self.value)
        self.weight = sum((ord(char) for char in self.value))

    def __modify(self, new_value: str) -> None:
        """This method should only be called from OOP of this variable"""
        if new_value == self.value: return

        if len(new_value) > self.length: self.verboseEvent.emit()
        elif len(new_value) < self.length: self.dverboseEvent.emit()
        
        if sum((ord(char) for char in new_value)) > self.weight:
            self.weightedEvent.emit()
        elif sum((ord(char) for char in new_value)) < self.weight:
            self.dweightedEvent.emit()
        
        self.value = new_value
        self.length = len(new_value)
        self.weight = sum((ord(char) for char in new_value))


class HobLStringOOP(HobLStringVariableStructure):

    def __init__(self, origin: HobLStringVariable,
                 name: HobLVariableName) -> None:
        super().__init__()
        self.origin = origin
        self.name = name
        self.setHobLProperties()

    def setHobLProperties(self) -> None:
        self._value = self.origin.value
        self.size = sys.getsizeof(self)
        self._length = len(self.value)
        self._weight = sum((ord(char) for char in self.value))

    def low(self) -> None: self.value = self.value.lower()
    def upr(self) -> None: self.value = self.value.upper()

    def do(self) -> None:
        raise NotImplementedError
        

class HobLFixedVariable(Protocol):

    name: HobLVariableName
    value: HobLNumber|str

    def __modify(self, new_value) -> None: ...


