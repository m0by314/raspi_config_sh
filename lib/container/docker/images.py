"""
Library to manage images with docker engine.
Uses the Low-level API of the sdk.
For more information visit:
    https://docker-py.readthedocs.io/en/stable/api.html
"""
import re

from lib.container.interface.images import ImagesBase
from lib.container.docker.client import DockerClient


class DockerImages(ImagesBase, DockerClient):
    """
    Manage Docker image on the server.

    Example:
        DockerImages().build(tag="test", path="dockerfile_path", rm=True))
        image_id = DockerImages().get("test")
        DockerImages().delete("test")
    """

    def get(self, name: str) -> str:
        """
        Gets image ID.
        :param name: The name of the image.
        :return: image ID
        :raises: NameError if image not found
        """
        response = self._con.images(quiet=True, filters={"reference": name})
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
        response = self._con.build(**kwargs)

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
        return self._con.remove_image(name)
