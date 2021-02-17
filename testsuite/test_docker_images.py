#!/usr/bin/env python
""" Unit tests for package lib.container.docker.images """
import unittest
import os
import site

site.addsitedir('..')
from lib.container.docker.images import DockerImages

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
        cls.cli = DockerImages()

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

    def test_get(self):
        """
        Test method DockerImages.get()
        """
        self.assertTrue(self.cli.get("alpine"))

    def test_get_raise_exception(self):
        """
        Test raise exception on the method DockerImages.get()
        """
        with self.assertRaises(NameError):  # needed to work well assertRaises
            self.cli.get("accttt")

    def test_get_raise_no_exception(self):
        """
        Test not raise exception on the method DockerImages.get()
        """
        try:
            self.cli.get("alpine")
        except NameError:
            self.fail("method get raised NameError unexpectedly!")

    def test_delete(self):
        """
        Test method DockerImages.delete()
        """
        self.assertTrue(self.cli.delete("test_build_true"))


if __name__ == '__main__':
    unittest.main()
