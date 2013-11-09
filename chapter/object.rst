The Object of my Desire
=======================

Now we have data that we can store and functions to easily and repeatable
manipulate that data but sometimes it is not enough. Many programming languages
use a paradigm called Object Oriented Programming (commonly referred to as
"OOP") that allows us to do many cool and complex things in a relatively
elegant way.

The primary feature of OOP is... you guessed it, Objects. An object is a named
collection of variables that is used as a template to create a data structure
that performs as specified on demand.

This may sound quite complicated but it just needs to be explained better.
Objects are a great way of conceptualizing real world objects in programming.
Say we wanted to create a representation of a cube in our code. We could use
collection data types like a dictionary or some such to store the data about
our cube. What would be even better, however, is to create an object that
defines how a cube should act and what kind of data it would store.

The first thing that needs to be done is to think about what kind of data we
want to store. For a cube it should have at least a size variable to store,
well, its size. Because we are defining a cube and each side should have the
exact same length we can use one size variable for all of the sides. This is a
fine representation of a cube, albeit very simplistic. Lets also decide we want
to store its position in a three dimensional space. For this we simply need to
store an; X, Y and Z variable to describe its position.

Now enough theory lets have a look at this object in some real code, namely
:ref:Python.

.. doctest::

   >>> class Cube(object):
   ...     def __init__(self):
   ...         self.size = 0
   ...         self.posx = 0
   ...         self.posy = 0
   ...         self.posz = 0
   >>> companion = Cube()
   >>> companion.size = 10
   >>> companion.size
   10

OK, some basic things to get out of the way. In :ref:Python objects should inherit
from the base object, this is why after we name our new "class" (the common name
for an object definition) we place ``(object)`` to denote that this class acts
like an object.

Objects often have "constructors" and sometimes "destructors" these are
functions (or "methods" as they are called when they are part of an object's
definition) that are called when, you guessed it again, the object is
constructed and/or destroyed.

Also often when defining classes/objects and their methods we use the
terms ``self`` or ``this`` to mean this instance of an object.

In the above example we use the :ref:Python object constructor ``__init__``
that takes an object instance as an argument (``self``) and will give its
variables their default values, in this case the integer ``0``.

Next we assign the variable `companion` as a new instance of the `Cube`
object by calling the object as if it where a function. Finally we set the
`size` variable of our new `Cube` object to ``10`` and finally we show that the
change worked.

Now we can create any number of `Cube` objects each with their own values by
creating a new instance just as we did above with `companion`.

Other languages employ different methods and keywords for using and creating
objects, classes, instances, etc. and is usually very easy to find on the web.

The Layer Cake
--------------

Another very useful feature of OOP is Inheritance. What this means is that one
object definition can be based on another, taking all its variables and methods
and building on top of them.

Lets just go straight to an example this time.

.. doctest::

   >>> class InSpace(object):
   ...     def __init__(self, posx=0, posy=0, posz=0):
   ...         self.posx = posx
   ...         self.posy = posy
   ...         self.posz = posz
   >>> class Cube(InSpace):
   ...     def __init__(self, size, posx=0, posy=0, posz=0):
   ...         super(Cube, self).__init__(posx, posy, posz)
   ...         self.size = size
   >>> destination = InSpace(1,posz=5)
   >>> destination.posx
   1
   >>> destination.posy
   0
   >>> companion = Cube(10)
   >>> companion.posx
   0

This time we are doing things a little different.

We start off with similar thing to before, we are just creating a new class to
define things that exist in a three dimensional space. However here we are
using default arguments to allow the constructor to optionally take the
position of an `InSpace` object only if it is given, otherwise that dimension
will be ``0``.

Next we define a new `Cube` object, this time instead of inheriting directly
from `object` we inherit from `InSpace`. This means that our new object will
have everything that `InSpace` has and can be used anywhere an `InSpace` object
is expected. For this objects constructor we tell it that we want the size
argument to be required and have the position arguments to default to ``0``
upon creation/initialization of this object.

In some languages, :ref:Python included, you will need to explicitly call the
constructor of the "parent" object if you want it to be executed. :ref:Python
uses the ``super`` function to make this a bit easier in :ref:Python 3 it is
even easier as ``super`` can be called with no arguments to do exactly the same
thing as above, but people are still using both so I show what works
everywhere. 

This is more language specific rather then general programming and so is not
something I will go into too deeply. Suffice to say that above we use ``super``
to get the object definition of the parent of `Cube` and then call its
constructor appropriately.

After we have defined our object hierarchy I have just done some example usages
of both classes including different ways to use the optional positional
arguments.

The Method to my Madness
------------------------

Now we can go about doing cooler things like giving special methods that only
cubes can use or even better adding methods to `InSpace` that allows every
object definition that inherits it to easily move around without having to
update its "children" such as `Cube`. In fact lets do just that!
