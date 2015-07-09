from test_1 import *

import unittest
class SimpleTest(unittest.TestCase):

# testcase:{'args': (), 'result': 44, 'fn': 'simplefn', 'kwargs': {'a': 2, 'b': 3}}
    def test_simplefn_1c419a(self):
        self.assertEqual(simplefn(*(), **{'a': 2, 'b': 3}), 44)

# testcase:{'args': (), 'result': 44, 'fn': 'simplefn', 'kwargs': {'a': 2, 'b': 4}}
    def test_simplefn_f8867a(self):
        self.assertEqual(simplefn(*(), **{'a': 2, 'b': 4}), 44)

# testcase:{'args': (), 'result': 44, 'fn': 'simplefn', 'kwargs': {'a': 12, 'b': 4}}
    def test_simplefn_df5434(self):
        self.assertEqual(simplefn(*(), **{'a': 12, 'b': 4}), 44)

# testcase:{'args': (), 'result': {'a': 16, 'v': -1.0}, 'fn': 'simplefntwo', 'kwargs': {'a': 12, 'b': 4, 'v': -3}}
    def test_simplefntwo_02010e(self):
        self.assertDictEqual(simplefntwo(*(), **{'a': 12, 'b': 4, 'v': -3}), {'a': 16, 'v': -1.0})

# testcase:{'args': (), 'result': {'a': 6, 'v': 4}, 'fn': 'simplefntwo', 'kwargs': {'a': 2, 'b': 4}}
    def test_simplefntwo_a96340(self):
        self.assertDictEqual(simplefntwo(*(), **{'a': 2, 'b': 4}), {'a': 6, 'v': 4})

# testcase:{'args': (), 'result': {'a': 5, 'v': 4}, 'fn': 'simplefntwo', 'kwargs': {'a': 3}}
    def test_simplefntwo_4e24b3(self):
        self.assertDictEqual(simplefntwo(*(), **{'a': 3}), {'a': 5, 'v': 4})

# testcase:{'args': (), 'result': 1, 'fn': 'simplefn', 'kwargs': {}}
    def test_simplefn_8ceadf(self):
        self.assertEqual(simplefn(*(), **{}), 1)

# testcase:{'args': (), 'result': 2, 'fn': 'simplefn', 'kwargs': {'a': 2}}
    def test_simplefn_bd92eb(self):
        self.assertEqual(simplefn(*(), **{'a': 2}), 2)

