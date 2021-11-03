#!/usr/bin/env python


from lib.virtualization_engine.docker.images import DockerImages
from lib.virtualization_engine.docker.client import DockerClient
from lib.virtualization_engine.docker.container import DockerContainer
import docker


print("________________________________")
cli = DockerClient()
docker_con = DockerContainer(cli)
docker_img = DockerImages(cli)

image_name = "raspct_ansible_test"
docker_img.build(tag=image_name,
                 path="/Volumes/Dev/rasp_config/images/ansible")
#docker_con.create(image="test")
c = docker_con.create(
    image=image_name,
    detach=True,
    volumes={'/Volumes/Dev/rasp_config/ansible': {'bind': '/etc/ansible', 'mode': 'rw'},
           '/Volumes/Dev/rasp_config/keys': {'bind': '/home/raspc/.ssh', 'mode': 'rw'}},
    name='raspct_ansible_cont'
)
docker_con.start(c)
print(type(c))
docker_con.stop(c)
docker_con.delete(c)
#docker_con.connect(c, "/bin/bash")
# print("----- IMAGES -------")
# print(c.version())


# print(DockerImages(c))
# print(img.get("alpine"))
# print(c)
# d = DockerImages()
# d.get_id("alpine")

# d.get("alpine")


# for line in r:
#     print(line)
# print(c.delete("ansible_tt"))
