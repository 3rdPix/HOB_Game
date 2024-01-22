import abc
from _collections_abc import _check_methods
from .variables import HobLVar, HobLNumberVariable
from PyQt6.QtCore import pyqtSignal


FLAGS: tuple = ('alter', 'increase', 'decrease', 'deletion', 'equals',
                'dequals', 'syncrod', 'dsyncrod', 'connected', 'dconnected',
                'verbose', 'dverbose', 'weighted', 'dweighted')


class NonValidHobLEventFlag(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class FlagLike(abc.ABC):
    """Abstract base class for implementing the flag-like protocol."""

    @abc.abstractmethod
    def __flagstr__(self):
        """Return the flag name in string format."""
        raise NotImplementedError
    
    @classmethod
    def __subclasshook__(cls, subclass) -> bool:
        if cls is FlagLike:
            return _check_methods(subclass, '__flagstr__')
        return NotImplemented
    

class HobLEventFlag(FlagLike):

    def __init__(self, flag) -> None:
        if flag in FLAGS: self._flag = flag
        else:
            raise NonValidHobLEventFlag(
                f"The indicator {flag} is not a valid HobL event flag")
        
    def __flagstr__(self):
        return self._flag
        

"""
Structure of events
"""

class HobLEventType(abc.ABC):
    """Abtract base class to define events"""

    trigger: pyqtSignal = pyqtSignal()

    @abc.abstractmethod
    def __eventstr__(self) -> str:
        """Return the event in var + flag string format"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def slotCall(self) -> None:
        """Calls for signal"""
        raise NotImplementedError
    
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        if __subclass is HobLEventType:
            return _check_methods(__subclass, '__eventstr__', 'slotCall')
        return NotImplemented
    
class alterEvent(HobLEventType):

    def __init__(self, element: HobLVar) -> None:
        element.alterEvent.connect(self.slotCall)
        self._var = element

    def slotCall(self) -> None:
        pass

    def __eventstr__(self) -> str:
        return f'[Event Type] {self._var.name} -> "alter"'
    
class increaseEvent(HobLEventType):

    def __init__(self, element: HobLNumberVariable) -> None:
        element.increaseEvent.connect(self.slotCall)
        self._var = element

    def slotCall(self) -> None:
        pass

    def __eventstr__(self) -> str:
        return f'[Event Type] {self._var.name} -> "increase"'
    
class decreaseEvent(HobLEventType):

    def __init__(self, element: HobLNumberVariable) -> None:
        element.decreaseEvent.connect(self.slotCall)
        
    def slotCall(self) -> None:
        pass

    def __eventstr__(self) -> str:
        return f'[Event Type] {self._var.name} -> "decrease"'