#!/usr/bin/env python

"""
Unit tests for package lib_docker
"""
import unittest
import os
import site

site.addsitedir('..')
from lib.container_manager.docker.docker_images import DockerImages
from lib.container_manager.manager import ImagesManager


TESTSUITE_FOLDER = os.path.join(os.getcwd(), "testsuite/")


class TestLibDocker(unittest.TestCase):
    """
    Test for the Camera class
    """

    @classmethod
    def setUpClass(cls):
        """
        Initialize docker client
        """
        cls.img_manager = ImagesManager(DockerImages())

    def test_get(self):
        """
        Test method ImagesManager().get()
        """
        self.assertNotEqual(self.img_manager.get("alpine"), None, "Error on method ImagesManager.get, images alpine "
                                                                  "not found")
        self.assertEqual(self.img_manager.get("atdtadt"), None, "Error on method ImagesManager.get, get an image that "
                                                                "does not exist")

    def test_build(self):
        """
        Test method ImagesManager().build()
        """
        print("/////////")
        print(TESTSUITE_FOLDER + "Dockerfile_false/")
        self.assertTrue(self.img_manager.build(tag="test_build_true",
                                               path=TESTSUITE_FOLDER + "Dockerfile_true/"))
        self.assertFalse(self.img_manager.build(tag="test_build_false",
                                                path=TESTSUITE_FOLDER + "Dockerfile_false/"))

    def test_delete(self):
        """
        Test method ImagesManager().delete()
        """
        self.assertTrue(self.img_manager.delete("test_build_true"))
        self.assertFalse(self.img_manager.delete("test_build_false"))


if __name__ == '__main__':
    unittest.main()
