"""
Library to connect with docker engine.
Uses the Low-level API of the sdk.
For more information visit:
    https://docker-py.readthedocs.io/en/stable/api.html
"""
import docker
from .base import ClientBase


class DockerClient(ClientBase):

    @classmethod
    def _connect(cls, **kwargs):
        url = None

        if kwargs["url"]:
            url = kwargs["url"]

        cls._con = docker.APIClient(base_url=url)

    @property
    def connector(self) -> object:
        """
        Get the docker client object.
        :return: docker client object
        """
        return self._con
