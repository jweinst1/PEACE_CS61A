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

We were able to add a key:value pair to our cls object, and access it through the __dict__ container and a . command. Now, lets experiment with some different ways to change the key value pairs:

```
>>> cls.denero = 6
>>> cls.__dict__
{'denero': 6}
>>> cls.hilfinger = 'difficult'
>>> cls.__dict__
{'hilfinger': 'difficult', 'denero': 6}
```

Here, we discovered that a key value pair can be reassigned via dot commands, and we can bind new key:value pairs via dot commands as well. Now, what would happen if we bound a variable in the actual code of our sample class? Let's try it out:

```
class sample:
    GPA_cap = 3.3
    pass

>>> cls = sample()
>>> cls.__dict__
{}
>>> cls.GPA_cap
3.3
```

Uh oh, it appears we cannot access the variable GPA cap in our `__dict__` container, but we can access it through our dot expressions. We have run into what is called a class attribute:

> A class attribute is a key:value pair written in the frame of the classes code. This pair is not contained within the __dict__ container by default.

Now the question is, can we change class attributes with our dot expressions?

```
>>> cls.GPA_cap = 3.0
>>> cls.GPA_cap
3.0
```

The answer is yes we can. Since we have seen what class attributes are, let's explore what instance attributes, the key:value pairs inside the __dict__ container do differently.

> An instance attribute is a key:value pair stored in the object's __dict__ container, which is specific to every object of the class that is created.

Time to test out the difference bewteen them!

```
>>> oski = sample()
>>> bear = sample()
>>> oski.professor = 'John Denero'
>>> bear.professor = 'Paul Hilfinger'
>>> oski.GPA_cap = 4.0
>>> oski.__dict__
{'GPA_cap': 4.0, 'professor': 'John Denero'}
>>> bear.__dict__
{'professor': 'Paul Hilfinger'}
>>> bear.GPA_cap
3.3
>>> oski.GPA_cap
4.0
```

Ok, we did a lot of new things here, so lets go over them blow by blow.

1. Seperate instances of a class have seperate __dict__ containers, and thus seperate instance attributes. Assigning the professor name to the key Paul Hilfinger for oski DOES NOT change the name:key pair in bear for the professor name.
2. The command `oski.GPA_cap = 4.0` binds a key:value pair to the `oski.__dict__`, creating an instance attribute of the same name as the class attribute. Doing this, does not change the GPA cap for bear, because it only created an instance attribute, while bear only has the class attribute.

Now, continuing, lets see what happens to the oski GPA cap when we reassign it with sample:

```
>>> sample.GPA_cap = 3.0
>>> oski.GPA_cap
4.0
>>> bear.GPA_cap
3.0
```

From this, we can see that changing the class attribute on the class name, changes the class attribute for all instances of an object. Therefore,

> If an object has an instance attribute by the same name of the class attribute, you can only access the instance attribute through that object. Changing the class attribute by reassignment changes the class attribute for all instances of the class which do not have an instance attribute by the same name.

You might be wondering at this point, how does a class store its attributes. Each class also has a `__dict__` container!

```
>>> sample.__dict__
mappingproxy({'__doc__': None, '__weakref__': <attribute '__weakref__' of 'sample' objects>, '__module__': 'Classes.Tutorial', '__dict__': <attribute '__dict__' of 'sample' objects>, 'GPA_cap': 3.0})
```

Although the `__dict__` container for classes is more complicated, you can clearly see the gpa cap attribute at the end of the mappingproxy.

###Methods

####The init method

So, we have learned about class attributes and instances attributes. However, what if we wanted to, upon creating an instance of a class, give it some preset instance attributes, without doing `object.__dict__[name] = value`? We can give our class called a function, called `__init__`, that gives an object those predefined instance attributes were looking for.

```
class student:

    def __init__(self, GPA, professor):
        self.GPA = GPA
        self.professor = professor
        
        
>>> tom = student(3.1, 'Hug')
>>> tom.GPA
3.1
>>> tom.professor
'Hug'
>>> tom.__dict__
{'GPA': 3.1, 'professor': 'Hug'}
>>> student.__dict__
mappingproxy({'__weakref__': <attribute '__weakref__' of 'student' objects>, '__init__': <function student.__init__ at 0x1030aba60>, '__doc__': None, '__dict__': <attribute '__dict__' of 'student' objects>, '__module__': 'Classes.Tutorial'})
```

Here, we created a new class called student, and gave him an init function, which assigns two key:value pairs to the `__dict__` container of the object. Essentially, the init function is equivalent to this set of arguments:

```
tom.__dict__['GPA'] = 3.1
tom.__dict__['professor'] = 'Hug'
```

#####The Self statement

The `self` word in python refers to the instance of the class that the classes method is being called on. Because classes can have many, many instances active at a single amount of time, the self keyword acts a distinction between what instance the method is called in.
