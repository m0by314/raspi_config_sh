""" Module for manage containers"""
from lib.container_manager.images_interface import ImagesBase


class ImagesManager:
    """
    Manage Images

        Example: ImagesManager(DockerImages())

    Args:
        client: ImagesBase object
    """
    def __init__(self, client: ImagesBase):
        if isinstance(client, ImagesBase):
            self.__client = client
        else:
            raise TypeError

    def get(self, img):
        """
        Gets an image.
        :param img: The name of the image.
        :return: image
        """
        return self.__client.get(img)

    def build(self, **kwargs) -> bool:
        """
        Build an image and return boolean.
        :param kwargs: Build parameters.
        :return: boolean
        """
        return bool(self.__client.build(**kwargs))

    def delete(self, name: str) -> bool:
        """
        Remove an image.
        :param name: The image name.
        :return: boolean
        """
        return bool(self.__client.delete(name))
