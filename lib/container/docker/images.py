"""
Library to manage images with docker engine.
Uses the Low-level API of the sdk.
For more information visit:
    https://docker-py.readthedocs.io/en/stable/api.html
"""
import re
import docker

from lib.container.images_base import ImagesBase


class DockerImages(ImagesBase):
    """
    Manage Docker image on the server.

    Example:
        import docker
        images = DockerImages()
    """

    def __init__(self, base_url: str):
        self.__cli = docker.APIClient(base_url=base_url)

    def get(self, name: str) -> str:
        """
        Gets image ID.
        :param name: The name of the image.
        :return: image ID
        :raises: NameError if image not found
        """
        response = self.__cli.images(quiet=True, filters={"reference": name})
        if not response:
            raise NameError("Image Not Found: " + name)
        return response[0].replace("sha256:", "")

    def build(self, **kwargs: dict) -> bool:
        """
        Build an image and return True if success.
        :param kwargs:
                path (str) – Path to the directory containing the Dockerfile
                fileobj – A file object to use as the Dockerfile. (Or a file-like object)
                tag (str) – A tag to add to the final image
                quiet (bool) – Whether to return the status
                nocache (bool) – Don’t use the cache
                                when set to True
                rm (bool) – Remove intermediate containers.
                            The docker build command now defaults to --rm=true,
                            but we have kept the old default of False
                            to preserve backward compatibility
                pull (bool) – Downloads any updates to the FROM image in Dockerfiles
                forcerm (bool) – Always remove intermediate containers,
                                 even after unsuccessful builds
                dockerfile (str) – path within the build context to the Dockerfile
                buildargs (dict) – A dictionary of build arguments
        :return: boolean
        """
        building = False
        response = self.__cli.build(**kwargs)

        for line in response:
            print(line)
            if re.search("Successfully", str(line)):
                building = True

        return building

    def delete(self, name: str) -> bool:
        """
        Remove an image and True if success. Similar to the docker rmi command.
        :param name: the image name.
        :return: boolean
        """
        return self.__cli.remove_image(name)
