#Creating Function and Class Objects in Python

###Function Objects

Normally, when one wants to write a function or a class, it has to be written it into a py file. We see examples like the following:
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

###Class Objects

The `exec()` command can also be used to create class objects without writing them implicitly in a py file or into the interpreter. This can be done by stringing together a simple class definition:
```
def class_object():
    exec('class one: pass')
    return locals()['one']
>>> f = class_object()
>>> f
<class 'one'>
>>> obj = f()
>>> obj
<one object at 0x103680198>
>>> obj.__dict__
{}
```
This technique gives us access to the creation of empty class objects, but more importantly empty object instances. In Python, one usually has to create classes with specific `__init__()` methods and others to properly assemble and call instances of those classes. However, we can essentially do the same in a much simpler way, by using a `__dict__` attribute of an empty object instance and adding attributes to it from two lists. One of the lists must be a list of strings for names:
```
def create_object(names, values):
    assert len(names) == len(values)
    exec('class one: pass')
    obj = locals()['one']()
    for i in range(len(names)):
        obj.__dict__[names[i]] = values[i]
    return obj

>>> func = make_function('help', 'pay', ['pay+=2', 'pay*=5', 'credit = pay//3', 'return credit'])
>>> test_obj = create_object(['help', 'interest', 'message'], [func, 0.5, 'please pay by thursday.'])
>>> test_obj.help(7)
15
>>> test_obj.interest
0.5
>>> test_obj.message
'please pay by thursday.'
```
The previous function creator can also be used here to create methods for our object instance, as demonstrated. We must assert the lengths of both lists are equal as every entry in `__dict__` must have a name and value. This technique is particularly useful since it allows the usage of an object instance as a form of data structure, further extending the usage of the key-value system.
