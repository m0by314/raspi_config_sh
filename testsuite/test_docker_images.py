#!/usr/bin/env python
""" Unit tests for package lib.container.docker.images """
import unittest
import os
import site

site.addsitedir('..')
from lib.virtualization_engine.docker.images import DockerImages
from lib.virtualization_engine.docker.client import DockerClient

TESTSUITE_FOLDER = os.getcwd()


class TestDockerImages(unittest.TestCase):
    """
    Unit test for the DockerImages
    """

    @classmethod
    def setUpClass(cls):
        """
        Initialize docker client
        """
        cls.cli = DockerImages(DockerClient())

    def test_build(self):
        """
        Test method DockerImages.build()
        """
        self.assertTrue(self.cli.build(tag="test_build_true",
                                       path=TESTSUITE_FOLDER + "/Dockerfile_true/",
                                       rm=True))

    def test_fail_build(self):
        """
        Test fail method DockerImages.build()
        """
        self.assertFalse(self.cli.build(tag="test_build_false",
                                        path=TESTSUITE_FOLDER + "/Dockerfile_false/",
                                        rm=True))

    def test_get_id(self):
        """
        Test method DockerImages.get_id()
        """
        self.assertTrue(self.cli.get_id("alpine"))

    def test_get_id_not_found(self):
        """
        Test method DockerImages.get_id() with unknown images
        """
        self.assertEqual(self.cli.get_id("acttt"), None, "Get_id should return none")

    def test_delete(self):
        """
        Test method DockerImages.delete()
        """
        self.assertTrue(self.cli.delete("test_build_true"))


if __name__ == '__main__':
    unittest.main()
