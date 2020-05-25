import unittest
def fib_while_test():
    assert fib_while(2) == 1, 'The 2nd Fibonacci number should be 1'
    assert fib_while(3) == 1, 'The 3rd Fibonacci number should be 1'
    assert fib_while(50) == 7778742049, 'Error at the 50th Fibonacci number'

def identity_test():
    print("ddddd")
    assert identity(20) == 21, 'should be 20'

if __name__ == '__main__':
    unittest.main()