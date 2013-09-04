Playground
==========

Put on your sneakers kids, we are going to the playground. When the day is out
we will rule the school... But less lame sounding, I promise.

Firstly we want to fire up the :term:`Python` :term:`Interpreter`. You can use
the default :term:`Interpreter` perfectly fine and many do. However if you want
some extra features to make learning and using the :term:`Python`
:term:`Interpreter` easier you might want to check out bpython_ or install it
using the following command::

    $ pip install bpython

Now open a new :term:`Python` :term:`Interpreter` using either::

    $ python

or if you chose to install bpython_::

    $ bpython

.. _bpython: http://bpython-interpreter.org/

You will be presented with :term:`REPL` environment that you can play around.
If anything goes bad or you want to start again you can close the
:term:`Interpreter` down using ``CTRL+D`` or executing this command on a new
line in the :term:`Python` :term:`Interpreter`::

    >>> exit()

Afterwards you can re-open it the same as before for a new environment.

New kid on the block
--------------------

This is our stomping ground so we need to learn how to start stomping to get
results!

The first piece of programming we will be learning is a simple expression.
Expressions are chunks of code that do something and return results.

There are a great many things you can do with expressions but for now lets just
try some simple math in our :term:`Python` :term:`Interpreter`:

.. doctest::

   >>> 1 + 2
   3
   >>> 1 / 2.0 * 20
   10.0
   >>> 1 / (2.0 * 20)
   0.025

Great so we have written some simple, but boring, mathematical expressions in
:term:`Python`! But the last two examples are a bit different. First, if you
didn't guess already, the symbol for multiplication in programming is the
asterisk (``*``) character and division is the forward slash (``/``) character.
But the last two examples are almost exactly the same except for the
parenthesis around the ``2.0 * 20`` expression in the final one.

The reason for the parenthesis is to solve one of the largest problems in
programming. OK well not specifically but give but bare with me for a moment.
One of the largest problems for new programmers, other then the syntax of the
language they have chosen, is understanding that the computer does not (and can
not) think the way they do. It has no clue what you want to do with your code.
This makes it very hard for a computer to figure out what the right thing to do
is, so often it doesn't even try.

In programming we need to make our intentions clear and preferably concise. Not
only does a computer have to understand what you mean but so do other humans.
This speaks to a balance that we need to find between telling the computer
exactly what to do to get it right, and being able to actually articulate, and
understand those commands ourselves. Remember that while you may understand
what you write today but if you come back in six months will it still make
perfect sense?

But we are getting ahead of ourselves a bit. We use the parenthesis in the last
example above because we want to divide 1 by the result of 2.0 multiplied
by 20. Whereas in the second example we are dividing 1 by 2.0 and then
multiplying the result of that by 20.

Can I have a locker next to yours?
----------------------------------

So we have some basic numbers and we can manipulate these numbers. What we need
to do now is store them. In programming we use variables to store information
under a (sometimes) easy to remember name. Instead of just saying ``100`` we can
store that number in a variable called ``distance`` to more easily remember what
the number does and what it means. Languages have many different ways to create
and interact with variables. Luckily :term:`Python` is a dynamic language (more on that
in the future) and we can just give any value a name really simply:

.. doctest::

   >>> distance = 100
   >>> distance
   100

Now that we have stored the speed variable we can use it in calculations
instead of the number and store the result.

.. doctest::

   >>> speed = distance / 20.0
   >>> speed
   5.0

The above is just a simple velocity calculation (I promise we will move away
from maths soon) that uses the stored ``distance`` variable we set earlier and
divides it by ``20.0``(the time it took for our imaginary vehicle to travel
that distance) and then stored the result in the variable called ``speed``.

The important thing here is not the maths, it is the fact that you can store
almost anything to a variable and use the variable instead of the actual value.
Now that distance is stored in a variable all we have to do is change the
distance value to something else and re-run the speed calculation and it will
use the new distance! OK not that exciting yet. But it will be.

He's Just Not My Type
---------------------

There are more things than numbers in the world of programming. And there is
much more than maths. Actually only very few programming fields are math heavy.
Mostly we deal with basic data types and manipulating them to become what we
want.

Generally speaking, there are only a few basic types of data we can use and
store.

Strings
~~~~~~~

A string is just text, any kind of text really. Some languages have different
ways of writing these but mostly a line of text enclosed with quotation marks
denotes a string.

.. doctest::

   >>> name = "Taylor \"Nekroze\" Lawson"

The above example works perfectly well in :term:`Python` to store a string of my name.
But there are some important things here. If a string is any text between two
quotation marks then how do we include the same quotation mark in our text? For
this we have *Escape Sequences* these are characters that have a backslash
(``\``) before them and are read as a single letter, rather than two letters. In
the case I presented we use ``\"`` to show that we don't want to end the string
but rather to include a quotation mark inside of it.

Now in :term:`Python` we have the ability to also use single quotation marks as well as
the double so we could have just as easily done the following:

.. doctest::

   >>> name = 'Taylor "Nekroze" Lawson'

And now it would work fine without using the *Escape Sequence* ``\"`` because
the ``"`` character would not close the string in this case. Which you use is
up to you in :term:`Python` however in some languages the single and double
quotation mark means different things.

For example sometimes we differentiate between a string and a character. A
character is just one letter and a string is a collection of characters. But,
dynamic languages to the rescue once more, :term:`Python` just takes either one
and stores is for you without complaining.

Actually quick note, in :term:`Python` we can also easily do multi line strings
by using a *Triple-Quoted String* which can use either single or double quotes
and works on multiple lines of text.

Numbers
~~~~~~~

In programming we split numbers into different categories. Some languages have
more categories than others. The main split is between an *Integer* and a
*Floating Point Number* (which is usually called a *Float*).

An *Integer* is any whole number; ``1, 2, 3, 4, 5,`` etc. Whereas a *Float* is
a number that has a decimal point such as ``1.1, 1.2, 1.3, 1.4, 1.5,`` etc.

There is a difference in these types, not just conceptually, but in the way the
computer handles them. *Floats* are harder for the computer to work with and
take more space to store them. Also *Floats* are a representation of a number,
they are not always accurate but are usually accurate enough.

Some languages also make a distinction between small and large numbers. Many
languages can have either an *Integer* or a *Long*. A long is mostly the same
as an integer however its maximum and minimum values are much larger than an
*Integer*. When it comes to *Float* there is a similarly larger version in many
languages called *Double*, which just means double the precision thus a longer
decimal point.

Once again in :term:`Python` we don't have to worry about the differences all
that much, If we want to use any type of number :term:`Python` will just store
it and keep on working.

Booleans
~~~~~~~~

*Booleans* are interesting. A *Boolean* value is either ``True`` or ``False``,
that is all they can store. Think of it like a switch that is either on or off.

Some languages allow many different things to be considered in *Boolean* terms.
For example in :term:`Python` (and most languages) ``0`` is equivalent to
``False`` and anything higher then and including ``1`` is the same as ``True``.
Later we will see other ways to use many types of data as *Booleans* as well.

Collections
~~~~~~~~~~~

This is where it can get a bit crazy. A collection at its simplest is just a
way of grouping other data types together to store a collection of "things".

Your basic collection is a *List*, which works exactly as you would expect.
Just add in your data and it is all stored together and can be manipulated as
you wish. For example:

.. doctest::

   >>> shades = ['white', 'black']
   >>> shades.append('grey')
   >>> shades
   ['white', 'black', 'grey']

This is how we make a *List* in :term:`Python` and add an element to it.
Because :term:`Python` is a powerful dynamic programming language we can store
any types we want in any given collection. However many other programming
languages require collections to be homogeneous, this means that all values
must be the same type.

There are many other types of collections. Another very common type is the
*Dictionary* (or *Hash Table*). These allow you to make a map of one data type to
another, like looking up something in a dictionary.

.. doctest::

   >>> favorite = {'color': 'black', 'language': ':term:`Python`'}
   >>> favorite['color']
   'black'

We have just created a dictionary, stored it in the ``favorite`` variable and
then given it some simple mappings. On the second line we look up what the
dictionary holds under the string ``color`` and retrieve it.

Later on we will look at classes which are kind of like collections but also
very different.

I Love it When a Plan Comes Together
------------------------------------

Using just the types of data above and learning how to manipulate them we can
make just about any piece of software we can imagine. No, really. Pretty much
every computer program ever written uses some form of the above data types
along with a series of tricks to manipulate and control them. It's kind of
beautiful if you think about it.

The goal is for you to learn how programming works, not just :term:`Python`.
Play around with these data types in the :term:`Python` :term:`Interpreter` to
get a better feel for how they work, because these things are almost entirely
universal in programming. And once you get the basic concepts behind
programming itself, the language you use becomes a trivial wrapper around your
thoughts. Now that is what **Code for Thought** is all about!

In the next chapter we will be looking at using functions and telling the
computer how to do a specific job.
