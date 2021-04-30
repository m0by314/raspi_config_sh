"""
Library to manage container with docker engine.
Uses the Low-level API of the sdk.
For more information visit:
    https://docker-py.readthedocs.io/en/stable/api.html
"""
import os
from lib.virtualization_engine.container_base import ContainerBase

# TODO add docsting and test
class DockerContainer(ContainerBase):

    def __init__(self, client):
        self._cli = client

    def create(self, **kwargs) -> str:
        """
        Create a container.

        :param kwargs:
            * image (str) – The image to run
            * command (str or list) – The command to be run in the container
            * detach (bool) – Detached mode: run container in the background
              and return container ID
            * name (str) – A name for the container
            * user (str or int) – Username or UID
            * tty (bool) – Allocate a pseudo-TTY
            * volumes (dict or list ) –
                 A dictionary to configure volumes mounted inside the container.
                 The key is either the host path or a volume name, and
                 the value is a dictionary with the keys:
                        bind The path to mount the volume inside the container
                        mode Either rw to mount the volume read/write, or ro to mount it read-only.
                 For example:

                     {'/home/user1/': {'bind': '/mnt/vol2', 'mode': 'rw'},
                     '/var/www': {'bind': '/mnt/vol1', 'mode': 'ro'}}

        Usage :
            docker_con.create(
                image=test_raspct_img,
                detach=True,
                volumes={'/Volumes/Dev/rasp_config/ansible': {'bind': '/etc/ansible', 'mode': 'rw'},
                         '/Volumes/Dev/rasp_config/keys': {'bind': '/home/raspc/.ssh', 'mode': 'rw'}},
                name='raspct_ansible_cont'
            )

        :return: container Id (str)
        """
        param = {
            'image': kwargs['image'] if 'image' in kwargs else None,
            'command': kwargs['command'] if 'command' in kwargs else None,
            'detach': kwargs['detach'] if 'detach' in kwargs else None,
            'name': kwargs['name'] if 'name' in kwargs  else None,
            'user': kwargs['user'] if 'user' in kwargs  else None,
            'tty': kwargs['tty'] if 'tty' in kwargs  else None,
            'volumes': None,
        }

        host_config = {}

        if 'volumes' in kwargs:
            k = kwargs['volumes']

            if isinstance(k, list):
                param['volumes'] = k

            if isinstance(k, dict):
                vol = []
                binds = []

                for key in k.keys():
                    vol.append(key)
                    if k[key]['mode']:
                        bind = key + ':' + k[key]['bind'] + ':' + k[key]['mode']
                    else:
                        bind = key + ':' + k[key]['bind']
                    binds.append(bind)
                param['volumes'] = vol
                host_config['binds'] = binds

        if host_config != {}:
            print(host_config)
            param['host_config'] = self._host_config(host_config)

        cr = self._cli.create_container(**param)

        return cr["Id"]

    def _host_config(self, config: dict) -> dict:
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
        return self._cli.create_host_config(binds=config['binds'])

    def start(self, container):
        self._cli.start(container)

    def stop(self, container):
        self._cli.stop(container)

    @staticmethod
    def connect(cont_id, cmd):
        c = "docker exec -ti " + cont_id + " " + cmd
        os.system(c)

    def delete(self, container: str, force: bool = False) -> bool:
        """
        Remove a container.

        :param container: (str) – The container to remove
        :param force: (bool) Force the removal of a running container (uses SIGKILL)

        :return: bool
        """
        self._cli.remove_container(container, force)
