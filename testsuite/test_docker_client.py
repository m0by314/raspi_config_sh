#!/usr/bin/env python
""" Unit tests for package lib.virtualization_engine.docker.client """
import unittest
import os
import site

site.addsitedir('..')

from lib.virtualization_engine.docker.client import DockerClient

TESTSUITE_FOLDER = os.getcwd()


class TestDockerClient(unittest.TestCase):
    """Unit test for the DockerClient."""

    def test_raise_connection_error(self):
        """Checks that a connection error exception is raised if the connection fails."""
        with self.assertRaises(ConnectionError):  # needed to work well assertRaises
            DockerClient(url="192.168.1.15:1234")

    def test_singleton(self):
        """Verify there is only one instance."""
        cli1 = DockerClient()
        cli2 = DockerClient()
        self.assertTrue(cli1 is cli2)


if __name__ == '__main__':
    unittest.main()
