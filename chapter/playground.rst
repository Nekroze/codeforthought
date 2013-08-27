Playground
==========

Put on your sneakers kids, we are going to the playground. When the day is out
we will rule the school.

Firstly we want to fire up the python interpreter. You can use the default
interpreter perfectly fine and many do. However if you want some extra features
to make learning and using the python interpreter easier you might want to
check out bpython_ or install it using the following command::

    $ pip install bpython

Now you can open a new python interpreter using either::

    $ python

or if you chose to install bpython_::

    $ bpython

.. _bpython: http://bpython-interpreter.org/

New kid on the block
--------------------

This is our stomping ground so we need to learn how to start stomping to get
results!

The first piece of programming we will be learning is a simple expression.
Expressions are chunks of code that do something and return results.

There are a great many things you can do with expressions but for now lets just
try some simple math in our python interpreter:

.. doctest::

   >>> 1 + 2
   3
   >>> 1 / 2 * 20
   10.0
   >>> 1 / (2 * 20)
   0.025

Great so we have written some simple, but boring, mathematical expressions in
python! But the last two examples are a bit different. First, if you didn't
guess already, the symbol for multiplication in programming is the asterisk
(`*`) character and division is the forward slash (`/`) character. But the last
two examples are almost exactly the same except for the parenthesis around the
`1 * 20` expression in the final one.

The reason for the parenthesis is to solve one of the largest problems in
programming. OK well not specifically. One of the largest problems for new
programmers other then the syntax of the language they have chosen is
understanding that the computer does not and can not think the way they do. It
has no clue what you want to do with your code. This makes it very hard for a
computer to guess what the right thing to do is, so often it doesn't even try.

In programming we need to make our intentions clear and preferably clean. Not
only does a computer have to understand what you mean but so do humans. This
speaks to a balance that we need to find between telling the computer exactly
what to do to get it right and being able to actually articulate and understand
those commands ourselves. Remember, you may understand what you write today but
if you come back in six months will it still make perfect sense?

But we are getting ahead of ourselves a bit. We use the parenthesis in the last
one example above because we want to divide 1 by 40. Whereas in the second
example we are dividing 1 by 2 and then multiplying the result of that by 20.

Can I have a locker next to yours?
----------------------------------

So we have some basic numbers and we can manipulate these numbers. What we need
to do now is store them. In programming we use variables to store information
under a, sometimes, easy to remember name. Instead of just saying `100` we can
store that number in a variable called `distance` to more easily remember what
the number does and what it means. Languages have many different ways to create
and interact with variables. Luckily python is a dynamic language (more on that
in the future) and we can just give any value any name really simply:

.. doctest::

   >>> distance = 100
   >>> distance
   100

Now that we have stored the speed variable we can use it in calculations
instead of the number and store the result.

.. doctest::

   >>> speed = distance / 20
   >>> speed
   5.0

The above is just a simple velocity calculation (I promise we will move away
from maths soon) that uses the stored distance and divides it by `20`, the time
it took for our imaginary vehicle to travel that distance and then we stored
the result in the variable called `speed`.

The important thing here is not the maths, it is the fact that you can store
almost anything to a variable and use the variable instead of the actual value.
Now that distance is stored in a variable all we have to do is change the
distance value to something else and re-run the speed calculation and it will
use the new distance! OK not that exciting yet. But it will be.

He's Just Not My Type
---------------------

There are more things then numbers in the world of programming. And there is
much more then maths. Actually only very few programming fields are math heavy.
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

The above example works perfectly well in python to store a string of my name.
But there are some important things here. If a string is any text between two
quotation marks then how do we include the same quotation mark in our text! For
this we have *Escape Sequences* these are characters that have a backslash
(`\`) before them and are read as a single letter, rather then two letters. In
the case I presented we use `\"` to show that we don't want to end the string
but rather to include a quotation mark inside of it.

Now in python we have the ability to also use single quotation marks as well as
the double so we could have just as easily done the following:

.. doctest::

   >>> name = 'Taylor "Nekroze" Lawson'

And now it would work fine without using the *Escape Sequence* `\"` because the
`"` character would not close the string in this case. Which you use is up to
you in python however some languages the single and double quotation mark means
different things. 

For example sometimes we differentiate between a string and a character. A
character is just one letter and a string is a collection of characters. But,
dynamic languages to the rescue once more, python just takes either one and
stores is for you without complaining.

Actually quick note, in python we can also easily do multi line strings by
using a *Triple-Quoted String* which can use either single or double quotes and
works on multiple lines of text:

.. doctest::

   >>> text = """Triple Quoted Strings:
   In this multi line string we can use 'single' and "double" quotes and end it
   on any line with another '''triple''' quote.
   """

Numbers
~~~~~~~

In programming we split numbers into different categories. Some languages have
more categories then others. The main split is between an *Integer* and a
*Floating Point Number*, which are usually just called *Float*.

An *Integer* is any whole number; `1, 2, 3, 4, 5,` etc. Whereas a *Float* is a
number that has a decimal point such as `1.1, 1.2, 1.3, 1.4, 1.5,` etc.

There is a difference in these types not just conceptually but in the way the
computer handles them. *Floats* are harder for the computer to work with and
take more space to store them. Also *Floats* are a representation of a number,
they are not always accurate but are usually accurate enough.

Some languages also make a distinction between small and large numbers. Many
languages can have either an *Integer* or a *Long*. A long is exactly the same
as an integer however its maximum and minimum values are much large then an
*Integer*. When it comes to *Float* there is a similarly larger version in many
languages called *Double*, which just means double the precision thus longer
decimal point.

Once again in python we don't have to worry about the differences all that
much, If we want to use any type of number python will just store it keep on
working.

Booleans
~~~~~~~~

Booleans are interesting. A *Boolean* value is either `True` or `False`, that
is all they can store. Think of it like a switch that is either on or it isn't.

Some languages allow many different things to be considered in *Boolean* terms.
For example in python (and most languages) `0` is equivalent to `False` and
anything higher then and including `1` is the same as `True`. Later we will see
other ways to use many types of data as *Booleans* as well.

Collections
~~~~~~~~~~~

This is where it can get a bit crazy. A collection at its simplest is just a
way of grouping other data types together to store a collection of "things".

Your basic collection is a *List*, which works exactly as you would expect.
Just add in your data and it is all stored together and can be manipulated as
you wish. For example:

.. doctest::

   >>> shades = ["white", "black"]
   >>> shades.append("grey")
   >>> shades
   ["white", "black", "grey"]

This is how we make a *List* in python and add an element to it. Because python
is a powerful dynamic programming language we can store any types we wont in
any given collection. However many other programming languages require
collections to be homogeneous, this means that all values must be the same
type.

There are many other types of collections. Another very common type is the
*Dictionary* or *Hash Table*. These allow you to make a map of one data type to
another, like looking up something in a dictionary.

.. doctest::

   >>> favorite = {"color": "black", "language": "python"}
   >>> favorite["color"]
   "black"

We have just created a dictionary, stored it in the `favorite` variable and
then given it some simple mappings. The second line we look up what the
dictionary stores under the value `"color"` and retrieve it.

Later on we will look at classes which are kind of like collections but also
very different.

I Love it When a Plan Comes Together
------------------------------------

Using just the types of data above and learning how to manipulate them we can
make just about any piece of software we can imagine. No really. Pretty much
every computer program ever written uses some form of the above data types
along with a series of tricks to manipulate and control them. It's kind of
beautiful if you think about it.

The goal is for you to learn how programming works, not just python. Play
around with these data types in the python interpreter to get a better feel for
how they work, because these things are almost entirely universal in
programming. And once you get the basic concepts behind programming itself, the
language you use becomes a trivial wrapper around your thoughts. Now that is
what **Code for Thought** is all about!

In the next chapter we will be looking at using functions and telling the computer how to do a
specific job.
