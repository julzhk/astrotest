# Astro-test
Capture functions arguments and results and create a unit test file for that combination to assist refactoring.

Why?
Imagine you have to refactor a large, undocumented (untested!) python code base.
You'd probably identify the most important, slowest, or most error-prone 
One strategy is to write tests for the more significant functions and work from there.
 
This proof-of-concept utility captures this initial functionality by generating test cases during test executions of the code.

Example
===

If the following function has the test_logging decorator:

    @test_logger
    def simplefn(a,b):
        return a+b
    
and is called with:

    simplefn(a=1,b=2)

it'll create a unit test: 
   

    # testcase:{'args': (), 'result': 3, 'fn': 'simplefn', 'kwargs': {'a': 1, 'b': 2}}
        def test_simplefn_1c419a(self):
            self.assertEqual(simplefn(*(), **{'a': 1, 'b': 2}), 3)
