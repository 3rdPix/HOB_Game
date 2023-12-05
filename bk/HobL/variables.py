import abc
from _collections_abc import _check_methods
import re


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


class HobLGhostAny:

    def __init__(self, name: HobLVariableName[str]) -> None:
        self.name = name


class HobLGhostEvent:

    def __init__(self, name: HobLVariableName[str]) -> None:
        self.name = name


def expect_event(ghostVar: HobLGhostAny) -> HobLGhostEvent:
    """Turns an unkwown variable type to a ghost event"""
    new = HobLGhostEvent(ghostVar.name)
    del ghostVar
    return new


class HobLNumberVariable:

    def __init__(self, name: HobLVariableName[str],
                 value: HobLNumber[int|float|str]) -> None:
        self.name = name
        self.value = value

    def __modify(self, new_value: HobLNumber[int|float|str]) -> None:
        """This method should only be called from OOP of this variable"""
        self.value = new_value


class HobLStringVariable:

    def __init__(self, name: HobLVariableName[str], value: str) -> None:
        self.name = name
        self.value = value

    def __modify(self, new_value: str) -> None:
        """This method should only be called from OOP of this variable"""
        self.value = new_value

