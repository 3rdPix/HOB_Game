import abc
from _collections_abc import _check_methods


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
        