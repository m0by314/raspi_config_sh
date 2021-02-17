""" Minimal interface to define a client"""
import abc


class ClientBase(abc.ABC):
    """
    Define method to client container
    """
    def __init__(self):
        self._con = None
        if not self.is_connected():
            self._connect()

    @property
    def con(self) -> object:
        """
        Object connection property
        :return: object
        """
        return self._con

    @abc.abstractmethod
    def _connect(self) -> object:
        """
        Connection to client
        :return: object
        """

    def is_connected(self) -> bool:
        """
        Check if the client is already connected
        :return: bool
        """
        return bool(self._con)
