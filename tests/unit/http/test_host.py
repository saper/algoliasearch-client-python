import unittest

from algoliasearch.http.host import Host


class TestHost(unittest.TestCase):
    def setUp(self):
        self.host = Host('foo.com')

    def test_url(self):
        self.assertEqual(self.host.url, 'foo.com')

    def test_priority(self):
        # Default priority test
        self.assertEqual(self.host.priority, 0)

        host_with_less_priority = Host('foo.com', 5)
        # Specific priority
        self.assertEqual(host_with_less_priority.priority, 5)

    def test_up(self):
        self.assertEqual(self.host.up, True)

    def test_retry_count(self):
        self.assertEqual(self.host.retry_count, 0)
