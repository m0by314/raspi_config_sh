""" Docker images """
import docker

from lib.container_manager.images_interface import ImagesBase


class DockerImages(ImagesBase):
    """
    Manage Docker image on the server.

    Example:
        import docker
        images = DockerImages()
    """

    def __init__(self):
        self.__cli = docker.from_env().images

    def get(self, name: str) -> str:
        """
        Gets an image.
        :param name: The name of the image.
        :return: image or None
        """
        try:
            image = self.__cli.get(name)
        except docker.errors.ImageNotFound as err:
            print(err)
            return None
        return image

    def build(self, **kwargs: dict) -> bool:
        """
        Build an image and True if success. Similar to the docker build command.
        Either path must be set.
        :param kwargs: build parameters.
        :return: boolean
        """
        try:
            self.__cli.build(**kwargs)
        except docker.errors.BuildError as err:
            print(err)
            return False
        return True

    def delete(self, name: str) -> bool:
        """
        Remove an image and True if success. Similar to the docker rmi command.
        :param name: the image name.
        :return: boolean
        """
        try:
            self.__cli.remove(name)
        except docker.errors.ImageNotFound as err:
            print(err)
            return False
        return True
