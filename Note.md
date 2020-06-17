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

## 1.5 Control
Practical Guidance. When indenting a suite, all lines must be indented the same amount and in the same way (use spaces, not tabs). Any variation in indentation will cause an error.

Python includes several false values, including 
* 0
* None
* False
* ''

 All other numbers are true values.

 0 == -0 True

 eq(1, 1.0) True

 In operator module, 
 * ge: >= 
 * eq: ==
 

#### short-circuiting

To evaluate the expression <left> and <right>:

* Evaluate the subexpression <left>.
* If the result is a false value v, then the expression evaluates to v.
* Otherwise, the expression evaluates to the value of the subexpression <right>.

To evaluate the expression <left> or <right>:

* Evaluate the subexpression <left>.
* If the result is a true value v, then the expression evaluates to v.

* Otherwise, the expression evaluates to the value of the subexpression <right>.


To evaluate the expression not <exp>:

* Evaluate <exp>; The value is True if the result is a false value, and False otherwise.

These values, rules, and operators provide us with a way to combine the results of comparisons. Functions that perform comparisons and return boolean values typically begin with is, not followed by an underscore (e.g., isfinite, isdigit, isinstance, etc.).



A while statement that does not terminate is called an infinite loop. Press <Control>-C to force Python to stop looping.


Doctests. Python provides a convenient method for placing simple tests directly in the docstring of a function. The first line of a docstring should contain a one-line description of the function, followed by a blank line. A detailed description of arguments and behavior may follow. In addition, the docstring may include a sample interactive session that calls the function:

```
>>> def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total
```

Testing: 

* python3 -m doctest -v 1.py

## 1.6 Higher-Order-Functions
Functions that manipulate functions are called higher-order functions.

Babylonia Method

Compute a's square root: converge

(x + a/x)/2

Critically, the inner functions have access to the names in the environment where they are defined (not where they are called).

The sqrt_update function carries with it some data: the value for a referenced in the environment in which it was defined. Because they "enclose" information in this way, locally defined functions are often called closures.


Newton's Method:

tangent: n. 切线，切面；正切
adj. 切线的，相切的；接触的；离题的

derivative: n.导数

differentiable functions 可导/微方程

A zero of a function f is an input x such that f(x)=0.


We can use higher-order functions to convert a function that takes multiple arguments into a chain of functions that each take a single argument. More specifically, given a function f(x, y), we can define a function g such that g(x)(y) is equivalent to f(x, y). Here, g is a higher-order function that takes in a single argument x and returns another function that takes in a single argument y. This transformation is called currying.

Some programming languages, such as Haskell, only allow functions that take a single argument, so the programmer must curry all multi-argument procedures.

The curry2 function takes in a two-argument function f and returns a single-argument function g. When g is applied to an argument x, it returns a single-argument function h. When h is applied to y, it calls f(x, y). Thus, curry2(f)(x)(y) is equivalent to f(x, y). The uncurry2 function reverses the currying transformation, so that uncurry2(curry2(f)) is equivalent to f.

lambda            x            :          f(g(x))

"A function that    takes x    and returns     f(g(x))"


notoriously illegible: 众所周知的不好辨认


Python provides special syntax to apply higher-order functions as part of executing a def statement, called a decorator.


```
def trace(fn):
    def wrapped(x):
        print('->', fn)
        return fn(x)
    return wrapped

@trace
def tripple(x):
    return 3 * x 


As usual, the function triple is created. However, the name triple is not bound to this function. Instead, the name triple is bound to the returned function value of calling trace on the newly defined triple function. In code, this decorator is equivalent to:

>>> def triple(x):
        return 3 * x
>>> triple = trace(triple)    
```

## 1.7
anatomy n.解剖学
factorial n.阶乘
unwind vt.解开，松开

recursive leap of faith

Mutual recursion: A calls B, B calls A

A function with multiple recursive calls is said to be tree recursive because each call branches into multiple smaller calls, each of which branches into yet smaller calls, just as the branches of a tree become smaller but more numerous as they extend from the trunk.

Tree recursion
当遇到一个问题时，试图从各个方向降级和拆分。

# Chapter2 Building Abstractions with Data
## 2.1 Introduction 
>>> type(2)
<class 'int'>

Python includes three native numeric types:
 * integers (int), 
 * real numbers (float), 
 * complex numbers (complex).


Abstraction barriers shape the way in which we think about data. A valid representation of a rational number is not restricted to any particular implementation (such as a two-element list);

```
>>> digits = [1, 8, 2, 8]

>>> digits * 2
[1, 8, 2, 8, 1, 8, 2, 8]

>>> [2, 7] + digits * 2
[2, 7, 1, 8, 2, 8, 1, 8, 2, 8]


```

Lists are a type of sequence, and sequences are iterable values.


This pattern of binding multiple names to multiple values in a fixed-length sequence is called sequence unpacking;


Ranges. A range is another built-in type of sequence in Python, which represents a range of integers. Ranges are created with range, which takes two integer arguments: the first number and one beyond the last number in the desired range.

```
>>> range(1, 10)  # Includes 1, but not 10
range(1, 10)

>>> list(range(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```



```
>>> odds = [1, 3, 5, 7, 9]
>>> [x+1 for x in odds]
[2, 4, 6, 8, 10]

>>> evens = [x+1 for x in odds]
>>> evens
[2, 4, 6, 8, 10]

>>> [x for x in odds if 25 % x == 0]
[1, 5]
>>> 

```

```
[<map expression> for <name> in <sequence expression> if <filter expression>]
```


aggregation  
 英  [ˌæɡrɪˈɡeɪʃn]   美  [ˌæɡrɪˈɡeɪʃn]

n. [地质][数] 聚合，聚集；聚集体，集合体

```
>>> len(city)
8
>>> city[3]
'k'

>>> 'Shabu ' * 2
'Shabu Shabu '

>>> '124' * 2
'124124'

>>> """The Zen of Python
claims, Readability counts.
Read more: import this."""

'The Zen of Python\nclaims, "Readability counts."\nRead more: import this.'

```


String Coercion. A string can be created from any object in Python by calling the str constructor function with an object value as its argument. This feature of strings is useful for constructing descriptive strings from objects of various types.

```
>>> str(2) + ' is an element of ' + str(digits)
'2 is an element of [1, 8, 2, 8]'
```

Adding state to data is a central ingredient of a paradigm called object-oriented programming. 


```
>>> chinese = ['coin', 'string', 'myriad']  # A list literal
>>> suits = chinese                         # Two names refer to the same list
As cards migrated to Europe (perhaps through Egypt), only the suit of coins remained in Spanish decks (oro).

>>> suits.pop()             # Remove and return the final element
'myriad'
>>> suits.remove('string')  # Remove the first element that equals the argument
Three more suits were added (they evolved in name and design over time),

>>> suits.append('cup')              # Add an element to the end
>>> suits.extend(['sword', 'club'])  # Add all elements of a sequence to the end
and Italians called swords spades.

>>> suits[2] = 'spade'  # Replace an element
giving the suits of a traditional Italian deck of cards.

>>> suits
['coin', 'cup', 'spade', 'club']
The French variant used today in the U.S. changes the first two suits:

>>> suits[0:2] = ['heart', 'diamond']  # Replace a slice
>>> suits
['heart', 'diamond', 'spade', 'club']
>>> suits.reverse()
>>> suits
['club', 'spade', 'diamond', 'heart']
>>> suits.sort()
>>> suits
['club', 'diamond', 'heart', 'spade']
```

Lists can be copied using the list constructor function. Changes to one list do not affect another, unless they share structure.

```
>>> suits = ['a', 'b', 'c', 'd']
>>> nest = list(suits)
>>> nest
['a', 'b', 'c', 'd']
>>> len(nest)
4
>>> suits.append('e')
>>> suits
['a', 'b', 'c', 'd', 'e']
>>> nest
['a', 'b', 'c', 'd']
>>> nest[0] = suits
>>> nest
[['a', 'b', 'c', 'd', 'e'], 'b', 'c', 'd']
>>> suits.append('ddddddd')
>>> nest
[['a', 'b', 'c', 'd', 'e', 'ddddddd'], 'b', 'c', 'd']
>>> suits
['a', 'b', 'c', 'd', 'e', 'ddddddd']
```

is and is not
Python includes two comparison operators, called is and is not, that test whether two expressions in fact evaluate to the identical object. Two objects are identical if they are equal in their current value, and any change to one will always be reflected in the other. Identity is a stronger condition than equality.

A slice from the beginning to the end of the list is one way to copy the contents of a list.

```
>>> a = [11, 12, 13]
>>> b = a[1:]
>>> b
[12, 13]
>>> a
[11, 12, 13]
>>> 
```

Again, the values placed in this list are not copied. list(s) and s[:] are equivalent for a list s.

The statement x += y for a list x and iterable y is equivalent to x.extend(y), aside from some obscure and minor differences beyond the scope of this text.

Passing any argument to extend that is not iterable will cause a TypeError. The method does not return anything, and it mutates the list.

However, the methods for manipulating the contents of a list are not available for tuples because tuples are immutable.

Dictionaries were unordered collections of key-value pairs until Python 3.6. Since Python 3.6, their contents will be ordered by insertion. Since dictionaries were historically unordered collections, it is safest not to assume anything about the order in which keys and values will be printed.

Dictionaries do have some restrictions:

* A key of a dictionary cannot be or contain a mutable value.
* There can be at most one value for a given key.

This first restriction is tied to the underlying implementation of dictionaries in Python. The details of this implementation are not a topic of this text. Intuitively, consider that the key tells Python where to find that key-value pair in memory; if the key changes, the location of the pair may be lost. Tuples are commonly used for keys in dictionaries because lists cannot be used.