Introduction
============

While **Code for Thought** is designed for those who have never programmed, it
is not exactly designed for the computer illiterate. There are some assumptions
made by this book that I should get out of the way before we get started.

Requirements
------------

First and foremost we recomend and assume a :term:`POSIX` based environment.
This means either a *Linux* operating system, like Xubuntu_ which could be
installed as a virtual machine like VirtualBox_. Alternatively on windows you
could install Cygwin_, an easy way to get a :term:`POSIX` based environment in
windows for very few trade offs. All instructions in this book are given as
command line commands for a :term:`POSIX` environment. There may be equivalents
for your own setup that can be on the internet.

There are many many guides on the internet for how to setup these things, many
of which explain it all better then I could in the scope of this book.

Ontop of some kind of :term:`POSIX` based environment you are going to need to
install Python_ along with the packages called Setuptools_ and Pip_. Python_
will be the language we will be learning how to code in. It is a very nice to
read and concise language that is perfect for begginers learning the basic
concepts of programming. Setuptools_ and Pip_ will help us to install and
distribute Python_ packages.

In these environments there should be some kind of text/code editor you are
comfortable with using. Anything will do and you can change your mind and use
something else at any point. Personally I use Emacs_ which is a great editor
that has a long tradition in the programming world, although people say its
learning curve is quite steep. Many others use Vim_ but there are many others
and if it comes down to it windows notepad will work fine as well... However if
you want to go with something more like this then give NotepadPlusPlus_ a try.

This can all be done in pure windows obviously however programming in *Linux*
is just much nicer. If you wish to program in windows only (without Cygwin_)
you will need everything bar the :term:`POSIX` environment and a text editor
such as, at least, NotepadPlusPlus_ for editing code and be able to use the
command prompt to run your code. There may be mention of tools that are
different to use or non existant on windows. Most likely in these cases there
are alternatives that should not be too hard to find with a good Google_.

.. _Xubuntu: http://xubuntu.org/
.. _VirtualBox: https://www.virtualbox.org/
.. _Cygwin: http://www.cygwin.com/
.. _Python: http://python.org/
.. _Setuptools: https://pypi.python.org/pypi/setuptools/0.9.8
.. _Pip: https://pypi.python.org/pypi/pip/1.4.1
.. _Emacs: http://www.gnu.org/software/emacs/
.. _Vim: http://www.vim.org/
.. _NotepadPlusPlus: http://notepad-plus-plus.org/
.. _Google: http://www.google.com

Structure
---------

**Code for Thought** will take you through learning how to write your own code
from start to finish and around. By the end of this you will understand the
major concepts behind programming and the tools around it that can help make
your code better. You will learn how to test your code and make sure it works,
how to document it so that others can help contribute to your code and learn
how to contribute to other peoples code and make the world a better place. 

OK. maybe you won't be influencing the entire world by the end of this book but
today, more then ever, the world needs people who can program. Almost everyone
you know uses computers far more then they would have 15, 10 even 5 years ago.
Yet we are all just users, so few care to even think what is behind it all.
Truth is that in general it is simpler then you think. If more people can
innovate and contribute to the growing world of computers then that has to be
making the world at least a little better. Right!

This book will move slowly from concept to concept, focusing not just on
teaching you some information about programming but teaching you how to teach
yourself to program.

We start with an introduction to the basic concepts of programming with 
interactive examples. Then we move onto abstracting ideas into functions. Then
on to data structures. With these basics we will begin to construct simple
programs you can test out and tinker with. Then we will use example programs
and code to provide real life usage of the advanced concepts you will be
learning. As the projects we work with grow in size we will introduce new 
tools that can greatly help with programming. These include but are not limited
to things like; version control, unit-testing and documentation.

At the end we will have a more free form discussion (all be it rather one sided)
about programming concepts and tools for the future.

Dedication
----------

This book is dedicated to Elysha. **Code for Thought** is designed to help her
and others like her to learn code and better understand the second love of my
life.
