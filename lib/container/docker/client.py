"""
Library to connect with docker engine.
Uses the Low-level API of the sdk.
For more information visit:
    https://docker-py.readthedocs.io/en/stable/api.html
"""
from lib.container.interface.client import ClientBase
import docker


class DockerClient(ClientBase):
    """
    Create a client to communicate with docker engine
    """

    def _connect(self) -> object:
        """
        Connection to docker engine
        :return: Docker client object
        """
        self._con = docker.APIClient(base_url='unix://var/run/docker.sock')
        return self.con
