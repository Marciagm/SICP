def square_root_update(x, a):
    x = (x + a/x)/2
    return x

def cube_root_update(x, a):
    return (2 * x + a/(x * x))/3


def improve(update, close, guess=1, max_update=100):
    k = 0
    while not close(guess) and k < max_update:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x- y) < tolerance

def square_root(a):
    def update(x):
        return square_root_update(x, a)
    def close(x):
        return approx_eq(x*x, a)
    return improve(update, close)

def cube_root(a):
    return improve(lambda x: cube_root_update(x, a), lambda x: approx_eq(x*x*x, a))


def update_square_of_2(x):
    return x - (x*x-2)/(2*x)

def square_of_2(iterators=100):
    x = -10
    k = 1
    while not approx_eq(x * x, 2) and k < iterators:
        x = update_square_of_2(x)
        print(x)
        k = k+1
    return x

def update_x(x, f, df):
    return x - f(x)/df(x)
    
def power(x, n):
    if n == 0:
        return 1
    k = 1
    product = 1
    while k <= n:
        product, k = product * x, k+1
    return product

def nth_root_of_a(n, a):
    x = 1
    k = 1
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)

    while not approx_eq(power(x, n), a) and k < 1e3:
        x, k = update_x(x, f, df), k+1
        print(x)
    return x

def trace(fn):
    def wrapped(x):
        print('->', fn)
        return fn(x)
    return wrapped

