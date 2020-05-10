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