"""
BasicShape Class - Abstract base class for the Shapes hierarchy.
Uses abc.ABC and @abstractmethod to define a formal interface.
"""

from abc import ABC, abstractmethod


class BasicShape(ABC):
    """Abstract base class for all shapes."""

    def __init__(self):
        """
        Preconditions: None
        Postconditions: Protected attributes _area and _name initialized
        """
        self._area = 0.0
        self._name = ""

    @property
    def area(self):
        """Getter for _area."""
        return self._area

    @area.setter
    def area(self, value):
        """Setter for _area."""
        self._area = value

    @property
    def name(self):
        """Getter for _name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for _name."""
        self._name = value

    @abstractmethod
    def calc_area(self):
        """
        Abstract method - must be overridden in all subclasses.
        Calculates and stores the area in _area.
        """
        pass
