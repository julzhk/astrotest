import unittest
import io
from astrotest import astro_test, UnitTestFactory, HashableDict

def simplefn(a=1):
    return a

class GenerateDictSignaturesTests(unittest.TestCase):

    def testcallsimplefunctions_with_decorator_returns_default_result(self):
        logger_decorator = astro_test(f = simplefn)
        r= logger_decorator.__call__()
        self.assertEqual(r, 1)

    def testcallsimplefunctions_with_decorator_with_args_returns_result(self):
        logger_decorator = astro_test(f = simplefn)
        r= logger_decorator.__call__(2)
        self.assertEqual(r, 2)

    def testcallsimplefunctions_with_decorator_with_kwargs_returns_result(self):
        logger_decorator = astro_test(f = simplefn)
        r= logger_decorator.__call__(a=3)
        self.assertEqual(r, 3)

    def testcallsimplefunctions_get_signature(self):
        logger_decorator = astro_test(f = simplefn)
        logger_decorator.__call__()
        self.assertDictEqual(logger_decorator.data, {('simplefn', (), HashableDict()): 1})

    def testcallfunction_with_args_get_signature(self):
        logger_decorator = astro_test(f = simplefn)
        logger_decorator.__call__(2)
        self.assertDictEqual(logger_decorator.data, {('simplefn', (2,), HashableDict()): 2})

    def testcallfunction_with_kwargs_get_signature(self):
        logger_decorator = astro_test(f = simplefn)
        logger_decorator.__call__(a=3)
        self.assertDictEqual(logger_decorator.data, {('simplefn', (), HashableDict(a=3)): 3})

if __name__ == '__main__':
    unittest.main()

