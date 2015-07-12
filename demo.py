from astrotest import astro_test

@astro_test
def simplefn(a=1,b=2):
    return 'fixed'

@astro_test
def simplefntwo(a=1,b=2,v=4):
    return a+b + v


print simplefn(a=2,b=3)
print simplefn(a=2,b=4)
print simplefntwo(a=2,b=4)
print simplefntwo()
print simplefntwo(a=2)
print simplefntwo(a=3)
