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
