"""Minimal interface for images management."""
import abc


class ImagesBase:
    """Define method to manage images"""

    @abc.abstractmethod
    def get_id(self, name: str) -> str:
        """
        Define method to get image ID.
        :param name: The images name.
        :return: image ID
        """

    @abc.abstractmethod
    def build(self, **kwargs: dict) -> bool:
        """
        Define method to build an image.
        :param kwargs: builds parameters.
        :return: True if success or False.
        """

    @abc.abstractmethod
    def delete(self, name: str) -> bool:
        """
        Define method to remove an image.
        :param name: image name.
        :return: True if success or False.
        """
