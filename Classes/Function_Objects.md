#Creating Function and Class Objects in Python

Normally, when one wants to write a function or a class, we see examples like the following:
```
def row(x):
    x += 4
    return x - 1

class student:
    
    GPA = 3.3
    Age = lambda x: x*5
```
However, the exec() function in Python 3 can be used to create multiline functions in a single string. This gives a greater range of flexibility than the usage of lambdas:
```
>>> exec('def add_3(num):\n\tnum += 3\n\treturn num')
>>> add_3(9)
12
```
You can also have a user defined function return a function object, and bind a variable to that call:
```
def fobj():
    exec('def x(y):\n\treturn y')
    return locals()['x']
>>> g = fobj()
>>>g(8)
8
```
