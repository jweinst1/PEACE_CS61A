#Python Classes and Objects

Python, a simple, and easy to learn language synatactially, becomes rather difficult for new programmers once they start to tackle the object oriented side of the language. This tutorial, aims to teach the concepts of classes, instances, and objects, from a low-level perspective, so the syntax on the surface makes sense on a conceptual level. 
###Objects

Objects in python, can be essentially interpreted in two ways. One, we can use the first definition:

> An object is an instance of a class.

This definition is rather vague and doesn't really tell us much about objects. Let's explore the second definition i like to refer to:

> An object is the binding of a variable, to a collection of names bound to values, called a class, where those values can be functions, integers, strings, lists, tuples, and more.

Ok, now were getting somewhere! An object is a binding, to a collection of names and values. Now, lets explore how these methods, values and more are stored in an object.

####The __dict__ container

Every user defined class has an attribute called `__dict__`. When called, it will display the names and values of each attribute of the object. Lets try this example:
```
class sample:
    pass

>>> cls = sample()
>>> cls
<Classes.Tutorial.sample object at 0x1030b8dd8>
>>> cls.__dict__
{}
```

Here, we created the simplest class possible, one that does absolutely nothing, it just has a pass statement. We bound that class to a value, `cls`, and then accessed its `cls.__dict__` container. This container, functions just like a python dictionary, pairing keys to values. However, it allows key to be accessed via dot commands, in the form <object>.<name>:

```
>>> cls = sample()
>>> cls.__dict__['denero'] = 'cs61a'
>>> cls.__dict__['denero']
'cs61a'
>>> cls.denero
'cs61a'
>>> cls.__dict__
{'denero': 'cs61a'}
```
