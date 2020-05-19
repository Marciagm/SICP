## 1.1 Getting Started
### Shortcut

Interactive controls. Each session keeps a history of what you have typed. To access that history, press 

```
<Control>-P (previous)
<Control>-N (next)
<Control>-D exits a session
```

### Basic knowledge
* Statements & Expressions.
* Functions
* Objects
* Interpreters

*functions are objects, objects are functions, and interpreters are instances of both.*


* Errors

>Learning to interpret errors and diagnose the cause of unexpected errors is called debugging.

Tips

* Test incrementally
* Isolate errors*
* Check your assumptions
* Consult others


## 1.2 Elements of Programming
Every powerful language has three such mechanisms:

* primitive expressions and statements, which represent the simplest building blocks that the language provides,
* means of combination, by which compound elements are built from simpler ones, and
* means of abstraction, by which compound elements can be named and manipulated as units.


reverse a tring:

》'draw'[::-1]
'ward'

The possibility of binding names to values and later retrieving those values by name means that the interpreter must maintain some sort of memory that keeps track of the names, values, and bindings. This memory is called an **environment**.

With multiple assignment, all expressions to the right of = are evaluated before any names to the left are bound to those values. As a result of this rule, swapping the values bound to two names can be performed in a single statement.

* Pure functions 
* Non pure functions

## 1.3 Defining New functions

* The user-defined function is not built into the interpreter.

* User-defined functions are used in exactly the same way as built-in functions.

**Function Signatures.** Functions differ in the number of arguments that they are allowed to take. To track these requirements, we draw each function in a way that shows the function name and its formal parameters. The user-defined function square takes only x; providing more or fewer arguments will result in an error. A description of the formal parameters of a function is called the function's signature.

The former is normal division, so that it results in a floating point, or decimal value, even if the divisor evenly divides the dividend:

5 / 4  is 1.25

8 / 4 is 2.0

The // operator, on the other hand, rounds the result down to an integer:

5//4 is 1

These two operators are shorthand for the truediv and floordiv functions.

python3 -i 1.py

doctest: 
python3 -m doctest -v 1.py
```
def square(x):
    """
    >>> square(5)
    25
    """
    return x * x

Trying:
    square(5)
Expecting:
    25
ok

```

default value of parameters

```
def sum(a, b=10):
    return a + b

print("values: ", sum(8, 9))
print("default values: ", sum(8))
```

## 1.4 Designing Functions
* Each function should have exactly one job.
* Don't repeat yourself is a central tenet of software engineering. 
* Functions should be defined generally.

### 1.4.1 Documentation

docstring
```
>>> def pressure(v, t, n):
        """Compute the pressure in pascals of an ideal gas.

        Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v

>>> help(pressure)
Help on function pressure in module __main__:

pressure(v, t, n)
    Compute the pressure in pascals of an ideal gas.
    
    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law
    
    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas
(END)

press q to quit
```
**Comment.** in Python can be attached to the end of a line following the # symbol. These comments don't ever appear in Python's help, and they are ignored by the interpreter. They exist for humans alone.

### 1.4.2 Default Argument Values
when call a function, the number of parameters is not fixed, since there may have default argument values.

## 1.5