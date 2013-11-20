RTFM!
-----

This is where we go from programming something that works to something that is
good and useful. In the programming world the difference between the scrawlings
of a mad man and the poetry of a genius is documentation. Even if you are the
only person who uses the code you are writing and it is not to be distributed
publicly, documentation is one of the most powerful tools a programmer has at
their disposal.

If you look around programming forums and discussions enough you will find
people talking about old code that they found from years ago that has no
documentation and they have no idea what it does. At the time they wrote the
code they could figure out what it did by looking at it but nowadays it makes
little or no sense. Documentation can help us just as much as it can help
others.

When starting a new programming project often you will come across a library
that seems like it would be useful but then you try and find out how to use it
but there is little or no documentation. At this point the only option to
figure it out is to read the code and learn it like that. Some people enjoy
this but others do not, especially if you are doing a large project that uses
many different libraries. If the documentation is lacking then it doesn't
matter how brilliant, fast, clean or effective the code is.

Having documentation is a great way to get people interested in how it works
and a very handy way of reminding yourself of the direction you are going.
Documentation often helps make your code more maintainable and even makes the
code itself more readable, as often documentation is included in the source
code itself. Writing or enhancing documentation is also a great way to learn
how someone elses project works. It is also a good introduction on how to
contribute to open source projects.

Documentation generally comes in two forms; comments and docs. Comments are
pieces of text that are inside the source code itself and is only viewed by
people looking at that code. Docs are sometimes, but not always, also included
in the source code and are turned into readable documentation for the public.
This can be done in multiple ways, nowadays the most common way is to generate
a website out of the docs and publicly publish that website... much the same
way this book is written. Actually that's exactly how this book is written.

This Title Explains the Content of This Sub-Chapter
===================================================

Not all programming languages agree on a common method of denoting a comment
but usually it is just a special character and then the rest of the line is
ignored by the programming language. This means anything after that special
character can only be seen by viewing the source code, sounds like the perfect
place to explain things.

Programmers are lazy folk, we do not want to remember everything about our
code and usually we can't. So what we often do is use a comment to describe
what some code does, especially when it isn't readily apparent what the code
really does.

Lets write some comments for our old 3d space example.

.. testcode::

   class InSpace(object):

       def __init__(self, posx=0, posy=0, posz=0):
           self.posx = posx
           self.posy = posy
           self.posz = posz

       def move_x(self, distance):
           self.posx += distance #Add distance to position x

       def move_y(self, distance):
           self.posy += distance #Add distance to position y

       def move_z(self, distance):
           self.posz += distance #Add distance to position z

   class Cube(InSpace):

       def __init__(self, size, posx=0, posy=0, posz=0):
           #Call the parent constructor.
           super(Cube, self).__init__(posx, posy, posz)
           self.size = size

Our code functions the same but we have now added some comments to explain what
is going on in some of the less obvious areas. In :term:`Python` comments are
started with the pound (``#``) character. Some languages us a double forward
slash (``//``) for single line comments and forward slash asterisk (``/*``) to
denote the start of a multi-line comment and the opposite to end that comment
(``*/``). While pound only does single line comments in :term:`Python` that
does not mean that we are missing out. There is wisdom in the way
:term:`Python` does things, instead of providing multi-line comments it
provides what it calls "doc strings" which are actually multi-line comments
however they are also documentation that can be accessed by the user of your
code and they look like strings. That's probably why they are called "doc
strings".

Unlike Humans, Chuck Norris Doesn't Need Documentation
======================================================

When learning how to use a piece of software one of the most useful things that
it can provide is clear, up to date, documentation. Lets go straight to writing
some documentation.

In :term:`Python` we can use a "doc string" to document a piece of code like a
class, a function, or a method.

Lets add some documentation to our 3d space code.


.. testcode::

   class InSpace(object):
       """
       Describes an object in a 3d environment.
       """
       def __init__(self, posx=0, posy=0, posz=0):
           self.posx = posx
           self.posy = posy
           self.posz = posz

       def move_x(self, distance):
           """Move on the X axis."""
           self.posx += distance #Add distance to position x

       def move_y(self, distance):
           """Move on the Y axis."""
           self.posy += distance #Add distance to position y

       def move_z(self, distance):
           """Move on the Z axis."""
           self.posz += distance #Add distance to position z

   class Cube(InSpace):
       """
       A Cube in 3d space.
       
       Stores a single size variable for the size of all edges.
       """
       def __init__(self, size, posx=0, posy=0, posz=0):
           #Call the parent constructor.
           super(Cube, self).__init__(posx, posy, posz)
           self.size = size

:term:`Python` has a handy ``help`` function that can output doc strings for
anything that is given to it. This is the basis of documentation in
:term:`Python` and can be used in more complex ways in the future. For example,
tools can be used that get all of the doc strings in your code and turn them
into a website, or file, that can be shared with the world.

For now give this example a go. Put the new documented 3d space classes into a
file and try using the ``help`` function to view the documentation.
