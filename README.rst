Astrotest
=========
Capture functions arguments and results and create a unit test file for that combination to assist refactoring.

Why would I want to do that?
----------------------------
Imagine you have to refactor a large, undocumented (untested!) python code base.
You'd probably identify the most important, slowest, or most error-prone
One strategy is to write tests for the more significant functions and work from there.

This proof-of-concept utility captures this initial functionality by generating test cases during test executions of the code.

Why 'Astrotest'?
================

'Astroturfing' is a term meaning to create inauthentic comments or discussion to influence or overwhelm
natural organic debate. Hence 'Astro-testing': it's not authentically TDD; it can create a large number of tests.

Overview
========

If the following function has the test_logging decorator::

  @astro_test
  def simplefn(a,b):
      return a+b

and if it's called with::

    simplefn(a=1,b=2)

it will create a unit test::

  def test_simplefn(self):
      self.assertEqual(simplefn(a=1, b=2), 3)

Detailed Example:
=================

create a 'generate_tests.py' file such as::

  from astrotest.astrotest import astro_test

  @astro_test
  def simplefn(a=1,b=2):
    return 'fixed output'

  @astro_test
  def simplefntwo(a=1, b=2, v=4):
    return a + b + v

  # now call the functions, to create unittests
  print simplefn(a=2, b=3)
  print simplefn(a=2, b=4)
  print simplefntwo(a=2, b=4)
  print simplefntwo()
  print simplefntwo(a=2)
  print simplefntwo(a=3)

executing this, creates a 'unittests.py' file, which will have the following auto-generated contents::

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