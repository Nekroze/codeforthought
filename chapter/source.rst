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
