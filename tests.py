import unittest
from test_gen import test_logger,UnitTestFactory,HashableDict

def simplefn(a=1):
    return a

class GenerateDictSignaturesTests(unittest.TestCase):

    def testcallsimplefunctions_with_decorator(self):
        logger_decorator = test_logger(f = simplefn)
        r= logger_decorator.__call__()
        self.assertEqual(r, 1)

    def testcallsimplefunctions_get_signature(self):
        logger_decorator = test_logger(f = simplefn)
        r= logger_decorator.__call__()
        self.assertDictEqual(logger_decorator.data, {('simplefn', (), HashableDict()): 1})

    def testcallfunction_with_args_get_signature(self):
        logger_decorator = test_logger(f = simplefn)
        r= logger_decorator.__call__(a=2)
        print logger_decorator.data
        self.assertDictEqual(logger_decorator.data, {('simplefn', (), HashableDict(a=2)): 2})

if __name__ == '__main__':
    unittest.main()

