import unittest

from astrotest.demo import *
class SimpleTest(unittest.TestCase):

# testcase:{'args': (), 'result': 'fixed', 'fn': 'simplefn', 'kwargs': {'a': 2, 'b': 3}}
    def test_simplefn_4a2010(self):
        self.assertEqual(simplefn(*(), **{'a': 2, 'b': 3}), 'fixed')

# testcase:{'args': (), 'result': 'fixed', 'fn': 'simplefn', 'kwargs': {'a': 2, 'b': 4}}
    def test_simplefn_1ba07a(self):
        self.assertEqual(simplefn(*(), **{'a': 2, 'b': 4}), 'fixed')

# testcase:{'args': (), 'result': 10, 'fn': 'simplefntwo', 'kwargs': {'a': 2, 'b': 4}}
    def test_simplefntwo_37813d(self):
        self.assertEqual(simplefntwo(*(), **{'a': 2, 'b': 4}), 10)

# testcase:{'args': (), 'result': 7, 'fn': 'simplefntwo', 'kwargs': {}}
    def test_simplefntwo_21317a(self):
        self.assertEqual(simplefntwo(*(), **{}), 7)

# testcase:{'args': (), 'result': 8, 'fn': 'simplefntwo', 'kwargs': {'a': 2}}
    def test_simplefntwo_a8ad0a(self):
        self.assertEqual(simplefntwo(*(), **{'a': 2}), 8)

# testcase:{'args': (), 'result': 9, 'fn': 'simplefntwo', 'kwargs': {'a': 3}}
    def test_simplefntwo_1bce4b(self):
        self.assertEqual(simplefntwo(*(), **{'a': 3}), 9)

# testcase:{'args': (2,), 'result': 2, 'fn': 'simplefn', 'kwargs': {}}
    def test_simplefn_97dc25(self):
        self.assertEqual(simplefn(*(2,), **{}), 2)

# testcase:{'args': (), 'result': 3, 'fn': 'simplefn', 'kwargs': {'a': 3}}
    def test_simplefn_539aeb(self):
        self.assertEqual(simplefn(*(), **{'a': 3}), 3)

# testcase:{'args': (), 'result': 1, 'fn': 'simplefn', 'kwargs': {}}
    def test_simplefn_8ceadf(self):
        self.assertEqual(simplefn(*(), **{}), 1)

