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
:term:`Python`.

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

OK, some basic things to get out of the way. In :term:`Python` objects should inherit
from the base object, this is why after we name our new "class" (the common name
for an object definition) we place ``(object)`` to denote that this class acts
like an object.

Objects often have "constructors" and sometimes "destructors" these are
functions (or "methods" as they are called when they are part of an object's
definition) that are called when, you guessed it again, the object is
constructed and/or destroyed.

Also often when defining classes/objects and their methods we use the
terms ``self`` or ``this`` to mean this instance of an object.

In the above example we use the :term:`Python` object constructor ``__init__``
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

In some languages, :term:`Python` included, you will need to explicitly call the
constructor of the "parent" object if you want it to be executed. :term:`Python`
uses the ``super`` function to make this a bit easier in :term:`Python` 3 it is
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

Using the above example, again, any changes in the code to the `InSpace` class
will be reflected in any class that inherits from it (it's children)
accordingly. Because of this we can easily abstract the concepts behind a class
in its base components. So if everything exists in a three dimensional space it
might be a good idea to implement things specific to being in such a space in a
class such as `InSpace` so each object that derives from it does not have to
implement such things over and over again. This leaves each object inheriting
from `InSpace` to focus on what it specifically needs to accomplish it's job.

With this in mind let us redefine the `InSpace` class with some methods to help
us move around in a space.

.. testcode::

   class InSpace(object):
       def __init__(self, posx=0, posy=0, posz=0):
           self.posx = posx
           self.posy = posy
           self.posz = posz

       def move_x(self, distance):
           self.posx += distance

       def move_y(self, distance):
           self.posy += distance

       def move_z(self, distance):
           self.posz += distance

With this as our new base class we can use the ``move_`` methods from any
object that inherits from `InSpace`.

This means that we can use the `Cube` class as it was defined above and do
``companion.move_x(10)`` to move ``10`` units forward in space and
``companion.move_x(-10)`` to move ``10`` units backwards. Note that in the
function call to move backwards we use ``-10`` for a specific reason.

We could have a method for moving forwards and backwards on each axis but that
may get a little messy. Instead we use a more general approach. When we add the
distance to a variable we use the ``+=`` operator which adds ``distance`` to
the current value of the variable on the left and then stores the result in the
same place. Basically the final two statements are identical.

.. doctest:: 

   >>> position = 0
   >>> position = position + 10
   >>> position += 10

Now comes the part that we abuse to make the movement three simple methods
instead of six. When you add a negative number (``-10`` in our case) to another
number it will actually perform a minus operation. By using this we can just
hand the move methods positive numbers when we want to move forward on that
axis and a negative integer when we want to move backwards. Neat huh!

This Isn't Even my Final Form
-----------------------------

It doesn't end here. Depending on you needs and what you language of choice
provides you can create powerful base classes or even interfaces that
you can use to make your code easily re-usable and even extendable.

Some languages allow a class to inherit from multiple classes at once. In
statically typed languages there is often :term:`Templating` which allows for
you to make a generic class that can be used with any object type. There are
very few problems that cannot be solved using an OOP approach.

It sounds complex but this can be super helpful. However just the basics
outlined here is more then enough to get you into the world of OOP and open up
a lot of possibilities for better code.
