import this
# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
import math
a = 5
print(math.sqrt(a))
print(globals())
# d = 1
def square(x):
    global a
    a = x ** 2
    d = x ** 2
    print(locals())
    def even(x):
        nonlocal d
        d = x / 2
        if d % 2 == 0:
            print('Чётное')
        else:
            print('Нечётное')
    return a

a = 5
b = square(2)
print(b)
from math import *
print(globals())
