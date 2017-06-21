'''Using third party library matplotlib\
   we need to import the library first'''

import matplotlib.pyplot as plt #I am importing this as plt, but you can import as you like

x = range(-100,100) # creats a list of number from -100 to 100 with a difference of 1
y = []
for i in x:
    sq_x = i**2
    y.append(sq_x)

'''we can easily do this by using numpy library, which I have not mentioned yet. So I am sticking with the \
   basic syntax by using a for loop and lists.'''

plt.plot(x,y)
plt.show()

''' Please read examples of matplotlib in detail at http://matplotlib.org/examples/index.html'''


