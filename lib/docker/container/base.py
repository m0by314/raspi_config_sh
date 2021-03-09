""" Minimal interface for container class management"""
import abc
from ..client import DockerClient


class ContainerBase(DockerClient):
    """
    Interface for container class
    """
    @abc.abstractmethod
    def create(self, **kwargs) -> bool:
        """
        Define create container method
        :param kwargs: builds parameters
        :return: bool
        """

    @abc.abstractmethod
    def delete(self, container: str) -> bool:
        """
        Define delete container method
        :param container: the container to remove
        :return: bool
        """
