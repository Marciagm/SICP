def trace(fn):
    def wrapped(x):
        print('fn(', x, ')')
        return fn(x)
    return wrapped

def sum_digits(num):
    if num < 10:
        return num
    num, last = num // 10, num % 10    
    return sum_digits(num) + last

def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def is_even(n):
    if n == 0:
        return True
    if n-1 == 0:
        return False    
    return is_even(n-2)

def move_pebbles(n):
    if n == 1:
        return True
    else:
        
        move_pebbles(n-1) 

def Alice_move_pebbles(n):
    if n == 0:
       print("Bob wins")
    else:
        Bob_move_pebbles(n-1)

def Bob_move_pebbles(n):
    if n == 0:
        print("Alice wins")
    
    if is_even(n):
        Alice_move_pebbles(n-2)
    else:
        Alice_move_pebbles(n-1)    

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)
    
def inverse_cascade(n):    
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)



def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n, m-1) + count_partitions(n-m, min(n-m, m))
            