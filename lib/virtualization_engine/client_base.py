""" Minimal interface to define a virtualization engine client."""
from abc import abstractmethod


class ClientBase:  # pylint: disable=too-few-public-methods
    """Singleton to initialize a communication with the virtualization engine client."""

    # connector
    __con = None

    def __new__(cls, **kwargs):
        """
        Create an unique connector with the virtualization engine client.

        :param kwargs: parameter received when creating the class,
                       contain the client connection parameters
        """
        if cls.__con is None:
            cls.__con = cls._connect(**kwargs)

        return cls.__con

    @staticmethod
    @abstractmethod
    def _connect(**kwargs):
        """
        Method to connect to virtualization engine client.

        :param kwargs: connection parameters
        """
