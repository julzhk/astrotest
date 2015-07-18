# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='astrotest',
    version='0.1.1',
    author=u'Julian Harley',
    author_email='astrotest.20.learningfuture@spamgourmet.com',
    packages=['astrotest'],
    url='https://github.com/julzhk/autogenerate_functional_tests',
    license='GNU licence, see LICENCE.txt',
    description='Auto generate unit-tests for a function from'
                ' executions of the function.'
                '',
    long_description='''# Astro-test
Capture functions arguments and results and create a unit test file for
that combination to assist refactoring.

Why?
Imagine you have to refactor a large, undocumented (untested!) python code base.

This utility captures a functions behaviour by generating test cases during
test executions of the code.

Why 'Astrotest'?
===

'Astroturfing' is a term meaning to create inauthentic comments or discussion
to influence or overwhelm natural organic debate.
Hence 'Astro-testing': it's not authentically TDD and it can create
a large number of test.
''',
)