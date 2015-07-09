from test_gen import test_logger

@test_logger
def simplefn(a=1,b=2):
    return 'bbb'

@test_logger
def simplefntwo(a=1,b=2,v=4):
    return a+b + v


print simplefn(a=2,b=3)
print simplefn(a=2,b=4)
print simplefntwo(a=2,b=4)
print simplefntwo()
print simplefntwo(a=2)
print simplefntwo(a=3)
