import unittest
# from test_gen import test_logger,UnitTestFactory


# @test_logger
def simplefn(a=1,b=2):
    return 'bbb'

# @test_logger
def simplefntwo(a=1,b=2,v=4):
    return a+b + v


# class SimpleTest(unittest.TestCase):
#
#     def testAdd(self):  ## test method names begin 'test*'
#         self.assertEqual(0 + 1, 1)

# if __name__ == '__main__':
#     unittest.main()


print simplefn(a=2,b=3)
print simplefn(a=2,b=4)
print simplefntwo(a=2,b=4)
print simplefntwo()
print simplefntwo(a=2)
print simplefntwo(a=3)
for a in range(0,10):
    for b in range(0,10):
        for v in range(0,10):
            simplefntwo(a=a,b=b,v=v)
print '--'
