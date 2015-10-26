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
Let's say you want to create a more complex function though, with several lines of calls. This can be constructed using a list of strings that represent each command, with a format string. The list of commands can be looped through and concatenated, which will then be executed and return from the `locals()` dictionary.
```
def make_function(name, parameter, commands):
    func = 'def {name}({parameter}):'.format(name=name, parameter=parameter)
    for line in commands:
        func += '\n\t' + line
    exec(func)
    return locals()[name]

>>> func = make_function('help', 'pay', ['pay+=2', 'pay*=5', 'credit = pay//3', 'return credit'])
>>> func(8)
16
```
