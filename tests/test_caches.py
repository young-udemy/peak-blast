import unittest

from caches import DictCache


class DictCacheTestCases(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.cache = DictCache()

    def tearDown(self):
        super().tearDown()
        self.cache.flush()

    def test_without_ns_and_without_key(self):
        self.assertIsNone(self.cache.get('ns', 'key'))

    def test_without_ns_and_with_key(self):
        self.cache.set('ns', 'key1', 'my value')
        self.assertEqual(self.cache.get('ns', 'key1'), 'my value')
        self.assertIsNone(self.cache.get('ns', 'key2'))

    def test_with_ns_and_without_key(self):
        self.cache.set('ns1', 'key', 'my value')
        self.assertEqual(self.cache.get('ns1', 'key'), 'my value')
        self.assertIsNone(self.cache.get('ns2', 'key'))

    def test_replace_value(self):
        self.cache.set('ns', 'key', 'my value')
        self.assertEqual(self.cache.get('ns', 'key'), 'my value')

        self.cache.set('ns', 'key', 'my value 2')
        self.assertEqual(self.cache.get('ns', 'key'), 'my value 2')

    def test_flush(self):
        self.cache.set('ns', 'key', 'my value')
        self.assertEqual(self.cache.get('ns', 'key'), 'my value')

        self.cache.flush()
        self.assertIsNone(self.cache.get('ns', 'key'))
