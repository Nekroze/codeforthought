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
