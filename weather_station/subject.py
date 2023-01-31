from abc import ABC, abstractmethod

from observer import Observer


class Subject(ABC):

    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        """Register an observer

        :param observer: The observer to be registered
        :type observer: Observer
        """
    

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        """Remove an observer

        :param observer: The observer to be removed
        :type observer: Observer
        """
    

    @abstractmethod
    def notify_observers(self) -> None:
        """Notify observers of a change in state
        """
