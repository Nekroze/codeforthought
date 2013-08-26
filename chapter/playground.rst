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
already know, the symbol for multiplication in programming is the asterisk
(`*`) character and division is the forward slash (`/`) character. But the last
two examples are almost exactly the same except for the parenthesis around the
`1 * 20` expression in the final one.

The reason for the parenthesis is to solve one of the largest problems in
programming. OK well not specifically. One of the largest problems for new
programmers other then the syntax of the language they have chosen is
understanding that the computer does not and can not think the way you do. It
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
