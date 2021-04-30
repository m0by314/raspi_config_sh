""" Minimal interface for container management."""
import abc

# TODO add method
class ContainerBase:
    """Define method to manage images."""

    @abc.abstractmethod
    def create(self, **kwargs) -> bool:
        """
        Define method to create container.
        :param kwargs: builds parameters
        :return: bool
        """

    @abc.abstractmethod
    def delete(self, container: str) -> bool:
        """
        Define method to delete container.
        :param container: the container to remove
        :return: bool
        """
