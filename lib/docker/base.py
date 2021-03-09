""" Minimal interface to define a client"""
import abc


class ClientBase(abc.ABC):
    """
    Singleton to define to define the basics of a client
    """
    # class instance
    _instance = None

    # connector
    _con = None

    def __new__(cls, *args, **kwargs):
        """
        Create an instance and a connector if it does not exist
        """
        if cls._instance is None:
            print("Create object")
            cls._instance = super(ClientBase, cls).__new__(cls)

        if cls._con is None:
            print("client connection")
            cls._connect(**kwargs)

        return cls._instance

    @classmethod
    @abc.abstractmethod
    def _connect(cls, **kwargs):
        """
        Class method to connect to the client
        :param kwargs: connection parameters
        """

    @abc.abstractmethod
    def connector(self) -> object:
        """
        Get connection object
        :return: object
        """
