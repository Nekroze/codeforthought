Tasty Source
============

When all is said and done writing code in a clean, readable, and reusable way
is pointless unless the code can be saved for later use. In programming a
source file (sometimes called a module) is a text file that contains our code.
Separating code into smaller modular files that refer to code in one another
module makes our code easier to read and edit because we can keep each concept
stored in a single file. We do not have to, nor should we, keep all of our
source code in the same file. This also makes redistributing or sharing the
code very easy.

If you have not noticed, much of the goal in programming is to break down your
thoughts into smaller concepts and then make them into even smaller pieces of
code. If you have one massive function that does everything your program needs
to do then it can often be hard to find and solve problems in this code.
However, if you break your code into smaller pieces (wherever it makes sense to
do so) then you are left with small, replaceable, and reusable pieces of the
puzzle.

Also probably evident, in programming we want to create beautiful code while
also being super lazy. This means that we tend to favor clean, small code that
when read is clear about what it does. This is made even easier when the source
code is not a big jumbled mess.

Pass the Source
---------------

Obviously if we split our code into different files we will need a method of
telling one file that it uses something in another file. Today this is usually
called "importing" (sometimes called include) and is often written at the top
of a source file. Importing is used not just to reference your own code in
other files but other code that is included in your programming language of
choice, or even a library that someone else wrote that you wish to use.

In :term:`Python` we can write the following code which will calculate ``2`` to
the power of ``10`` using the ``math`` module that comes with :term:`Python`.

.. doctest::

   >>> import math
   >>> math.pow(2, 10)
   1024.0

By using the ``import`` keyword we have told the language (:term:`Python` in
this case) that it should look for a module named ``math`` so that we can use
the code defined in math.

When you ask to import something the language will go looking in some
predefined locations that it thinks the source code is likely to be. Usually it
will first look in the current directory that you or your root source file is
located in. Then it might search other locations that it thinks its libraries
will be installed to. This means that even though :term:`Python` comes with a
math module, if I wrote another :term:`Python` file in the same directory that
I started the ``python`` command line interpreter then that file would be
imported instead. This is because it looks there before looking in the
libraries included by :term:`Python`.

Most languages work in a very similar way. Some languages have Imports (or
includes) that work slightly differently or can be made more specific. In
:term:`C/C++` when another file is included then everything in that file is
brought into the current file as if it where written here. Meaning if there is
a function called ``pow`` in the file we are including and we also have one in
the source file after the include then it will override the previous ``pow``.

A similar thing can be done in :term:`Python` but it is not recommended for
exactly the reason I mentioned above. It pollutes your source code by importing
everything into the current :term:`Namespace`.

.. doctest::

   >>> from math import *
   >>> pow(2, 10)
   1024.0

While this is generally considered a bad thing to do in many modern programming
circles it does present something nice. We do not have to prefix any ``math``
usage with its :term:`Namespace`, we just call the ``pow`` function directly.
This may sound like a trade off that needs to be considered but many languages
have already beaten you to a beautiful solution, selective imports!.

If all we are going to do is use the ``pow`` function, and it is not going to
cause any confusion or conflicts with other code in our own module, why not
just import ``pow`` and nothing else. Seems logical, lets do that.

.. doctest::

   >>> from math import pow
   >>> pow(2, 10)
   1024.0

There we have it. We are now importing only what we use. There are arguments
for both this method and just importing only the ``math`` module,
:term:`Namespace` and all, however they are a little beyond this book. No one
here is trying to tell you how anything has to be done. But, I do encourage you
to experiment and decide what is best for your self.

As a final note on importing things in cool ways. What if we do only want to
import a specific function, or even then whole module, but we already have
something that has the same name in our current module that would cause
conflicts. A few languages will allow you to rename what you import,
:term:`Python` included.

.. doctest::

   >>> from math import pow as mathpow
   >>> mathpow(2, 10)
   1024.0
   >>> import math as realmath
   >>> realmath.pow(2, 10)
   1024.0

Using these two methods we can usually dance around any import conflicts and
land on some beautiful code.

Although when importing modules do be careful about "Circular Dependencies". If
module A imports module B which imports module A, this can be a real problem
and some languages will just fail to handle this at all if you are lucky. If
you are unlucky they may get stuck in a loop or not give you any hint as to why
it is failing.

Fair Shake of the Source
------------------------

Some languages do not have an interactive interpreter and must be used by
compiling/interpreting source files. In :term:`Python` we can do both.

Source files are plain text files that use a specific file extension (the last
few letters of a file name after a dot, ie. ``filename.txt`` the extension is
``.txt``) that can be edited using anything that can write a simple text file
although some editors have better support for programming.

Another important thing about source files is that they usually have some kind
of entry point. An entry point is usually a function called ``main`` that is
the start of our programs execution.

:term:`Python` is a little different but every language has its twists. We are
going to write a simple program that will just say ``Hello World!`` to the
user. This is a pretty program that is very often used as a first tutorial or
introduction to a specific programming language.

Source files for :term:`Python` are denoted by the ``.py`` file extension. So
here is ``greeting.py``

.. testcode::

   def greeter():
       print("Hello World!")

   if __name__ == "__main__":
       greeter()

Now if we run ``python greeting.py`` from the command line we will get our
greeting. Finally we touched on something where :term:`Python` may not be the
easiest language to demonstrate with. I will give a little explanation.

In most languages there is just some kind of ``main`` function or equivalent
entry point. Due to the nature of :term:`Python`  we need to jump through a few
hoops to do the same thing.

We could get the same results if we wrote the file like this.

.. testcode::

   def greeter():
       print("Hello World!")
   greeter()

.. testoutput::
   :hide:

   Hello World!

Or, for those of you who are a little sharper, you may have
noticed we can just make this a one line file and do the same thing still.

.. testcode::

   print("Hello World!")

.. testoutput::
   :hide:

   Hello World!

However we do not do this when we are writing a program. As a single file
script this works just fine but what if some other source files in our program
wanted to use ``greeting.py``. Give it a go and see what happens. If we change
the ``greeting.py`` source code to either of the previous two examples and then
open a new :term:`Python` interpreter with ``python`` on the command line in
the same directory as the ``greeting.py`` source file.

If we entered ``import greeting`` it would print out ``Hello World!`` which in
the second examples case means that just by importing the module the
``greeter`` function was called. However the first example will only call the
function when that source is the file being executed by python directly as we
did by calling ``python greeting.py`` making the ``greeting`` module have the
special ``__name__`` variable equal ``"__main__"``.

In this case it does not really matter if you understand why this happens just
that you know that with python that is how it is done.

If you are still having problems figuring out when to use which method just
take a moment to experiment. After all experimenting is the best way to learn
programming (in my opinion) and is a core concept of this book.
