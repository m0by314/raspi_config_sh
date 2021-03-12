"""
Docker daemon connection.

Using the Low-level API of the sdk.
For more information visit:
    https://docker-py.readthedocs.io/en/stable/api.html
"""

from docker import APIClient
from ..client_base import ClientBase


class DockerClient(ClientBase):  # pylint: disable=too-few-public-methods
    """
    Create a docker client

    Example:
        * Connection to docker daemon distant
            DockerClient(url='172.10.10.101:1234')

        * Connection to local docker Daemon
            DockerClient()

    For parameters see :meth:`~DockerClient._connect`
    """

    @staticmethod
    def _connect(**kwargs):
        """
        Connection to docker daemon.

        :param kwargs: url (str) URL to the Docker server.
                    For example, unix:///var/run/docker.sock or tcp://127.0.0.1:1234.
                    by default: unix:///var/run/docker.sock
        """

        param = {
            "base_url": kwargs.setdefault("url", "unix:///var/run/docker.sock"),
        }
        print("connect")

        try:
            _con = APIClient(**param)
        except Exception as err:
            raise ConnectionError(err) from err
        return _con
