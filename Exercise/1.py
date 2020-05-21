""" Our exercise code of chapter1 """
from urllib.request import urlopen
from operator import truediv, floordiv

shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
words = set(shakespeare.read().decode().split())
{w for w in words if len(w) == 6 and w[::-1] in words}
# print(words[0])

def square(x):
    """
    >>> square(5)
    25
    """
    return x * x

print(square(5))

print(5/4)
print(5//4)
t = 5 // 4
print(floordiv(5, 4))

def sum(a, b=10):
    return a + b

print("values: ", sum(8, 9))
print("default values: ", sum(8))

def absolute_value(x):
    if x < 0:
        return -x
    elif x == 0:
        return x
    else:
        return x

if not '':
    print(1)

def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x-1) + fib(x-2)

y = fib(10)    

def fib_while(x):
    if x <= 1:
        return x
    pre = 0
    curr = 1

    # start from 2
    k = 2
    while k < x:
        k = k + 1
        pre, curr = curr, pre + curr

    return curr