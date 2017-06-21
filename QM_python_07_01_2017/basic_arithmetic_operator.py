''' we do not import any library.\
    For complicated tasks such as differentiation, integration, \
    solving the linear or non-linear equaitons,\
    we can use (import) third party libraries or make our own coding\
    environment. We will talk about this later.'''

''' Details can be read at:https://www.tutorialspoint.com/python/python_basic_operators.htm'''

#Addition, Subtraction, Multiplication, division
a = 2
b = 3
c = a + b #spaces between the character does not matter 
d = a - b
e = a * b
f = a**b # power 2
g = a/b
h = a/float(b)
i = float(a)/b
print 'a = {} && b = {} '.format(a,b)
print 'a+b gives: ',c
print 'a-b gives: ',d
print 'a*b gives: ',e
print 'a**b gives: ',f
print 'a/b gives: ',g
print 'a/float(b) gives: {}, is this different from a/b?'.format(h)
print '**Be careful when dealing with a division in python 2.7.xxx'
print 'float(a)/b gives: {}, what about this one?'.format(i)
