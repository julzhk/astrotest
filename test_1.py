import unittest
from test_gen import test_logger,UnitTestFactory


@test_logger
def simplefn(a=1,b=2):
    return 44

@test_logger
def simplefntwo(a=1,b=2,v=4):
    if v<1:
        v=-1.000
    return {'a':a+b, 'v': v}


# class SimpleTest(unittest.TestCase):
#
#     def testAdd(self):  ## test method names begin 'test*'
#         self.assertEqual(0 + 1, 1)

# if __name__ == '__main__':
#     unittest.main()


print simplefn(a=2,b=3)
print simplefn(a=2,b=4)
print simplefntwo(a=2,b=4)
# print simplefntwo()
# print simplefntwo(a=2)
print simplefntwo(a=3)
print simplefn(a=12,b=4)
print simplefntwo(a=12,b=4,v=-3)
# for a in range(0,10):
#     for b in range(0,10):
#         for v in range(0,10):
#             simplefntwo(a=a,b=b,v=v)
print '--'


print '--'
