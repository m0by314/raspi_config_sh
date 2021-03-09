"""
Library to manage container with docker engine.
Uses the Low-level API of the sdk.
For more information visit:
    https://docker-py.readthedocs.io/en/stable/api.html
"""
from .base import ContainerBase


class DockerContainer(ContainerBase):

    def __init__(self, *args, **kwargs):
        self._con = self.connector

    def create(self, **kwargs) -> bool:
        if kwargs['volumes']:
            self._config()
        self._con.create_container(
            image, cmd, volumes=volumes,
            host_config=cli.create_host_config(binds=[
                '/home/user1/:/mnt/vol2',
                '/var/www:/mnt/vol1:ro',
            ]))

    def _config(self, **kwargs):
        """
        Create a dictionary for configure container

        Example:
            binding volumes:
                DockerContainer().config(binds=[
                                            '/home/user1/:/mnt/vol2',
                                            '/var/www:/mnt/vol1:ro',
                                            ])


        :param kwargs:
        :return:
        """
        self._con.create_host_config(**kwargs)

    def delete(self, container: str) -> bool:
        pass

