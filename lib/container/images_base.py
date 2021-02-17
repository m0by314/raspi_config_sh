""" Define interface for images class management"""
import abc


class ImagesBase(abc.ABC):
    """
    Interface for images class
    """
    @abc.abstractmethod
    def get(self, name: str) -> str:
        """
        Define method for get an image.
        :param name: The images name.
        :return: image or None
        """

    @abc.abstractmethod
    def build(self, **kwargs: dict) -> bool:
        """
        Define method for build an image
        :param kwargs: builds parameters
        :return: True if success or False
        """

    @abc.abstractmethod
    def delete(self, name: str) -> bool:
        """
        Define method for remove an image.
        :param name: image name
        :return: True if success or False
        """
