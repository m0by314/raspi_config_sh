import abc


class ContainerBase(abc.ABC):
    """
    Interface for container manager
    """
    @abc.abstractmethod
    def create(self, **kwargs):
        """
        Define create container method
        """
