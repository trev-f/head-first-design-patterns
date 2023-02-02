from abc import ABC, abstractmethod


class DisplayElement(ABC):
    @abstractmethod
    def display(self) -> None:
        """Display data"""
