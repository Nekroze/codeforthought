Form and Function
=================

Here we will be looking at functions and control flow statements that can be
used to simplify common instructions and separate usage and implementation.
Important concepts for any programming project.

What is your quest?
-------------------

Say we wanted to do a calculation. Say we wanted to do a calculation often. It
would be useful (increasingly so with added complexity) to separate the
calculation into a *function*.

*Functions* are sets of instructions that are executed whenever the function is
called by name and can optionally take in data and even provide an output.

Imagine we had a reason to count how many times the letter "``a``" is in a
given string and return the result. Instead of writing the instructions
required to perform this task each time it is needed we could write a function
that does it for us. For example in python we would do the following:

.. doctest::

   >>> def count_a(text):
   ...     count = 0
   ...     for letter in text:
   ...         if letter == "a":
   ...             count += 1
   ...     return count
   >>> count_a("A test sample")
   1

The above code presents a host of new programming features that will be covered
in this section.

Firstly we defined a function called ``count_a`` and told it to take one
parameter called ``text``. This parameter is our input that we will count.

The next line should be rather familiar by now. We are simply creating a
integer variable to store the count, which starts at zero.

Here is where things get interesting, control flow. We need to check over each
letter in the ``text`` variable and see if it is the letter we are looking for.
To accomplish this we have employed a for loop. For loops are very common in
programming however some languages have different types of for loops. In python
the for loop is more of a ``foreach`` loop, unfortunately it is not named as
such. Basically it takes any ``iterable`` value (more on that later but for now
its anything that can be looped over) and gives you each piece of that value
until there are no more pieces left. Here we have given the for loop the text
value and told it to call each piece of it ``letter``.

Next we introduce another new type of control flow called the if statement. An
if statement evaluates a boolean expression and then allows you to execute
instructions if it is true. The boolean expression we are using here is
``letter == "a"``. Meaning if the piece of the text parameter we are looking at
currently is the same as a string containing the letter ``a`` then the boolean
expression evaluates to true. The if statement, now having an expression that
equals true then executes its code. In this case that is to add ``1`` to the
``count`` variable.

When adding one to the ``count`` variable we are using the in place addition
operator ``+=`` because we want to store the result in the same place. we could
instead use the following:

.. code-block:: python

   count = count + 1

this would do the calculation of whatever is stored in the count variable plus
one and then store it into the count variable. This does the exact same thing
but is a little longer. However we could not just say ``count + 1`` and thats
it because that is an expression and that expression will return the sum of
count plus one but has no idea that it needs to be stored.

After the if statement the for loop will return to the top and get the next
``letter`` from ``text`` and do it all again until we have gotten to the end of
the input. 

Once all letters have been checked the ``count`` variable will now be storing
the exact amount of the letter ``a`` that are contained within the text that
this function is given. But its of no use to just count the letters and then
forget about it so we need to return the results using, you guessed it,
``return count``. By now it should be rather obvious that this will simply
return whatever is stored in the variable ``count`` back out to whatever has
called this function.

Finally we see our brand new function in action by calling ``count_a("A test
sample")`` return the result ``1``. In our function we only checked for the
letter ``a`` but we must remember that this is not the same as ``A`` as strings
are case sensitive. If we wanted to check for both lowercase and uppercase
``a`` we could change the boolean expression for the if statement to a little
to the following:

.. code-block:: python

  letter == "a" or letter == "A"

Then the if statement has two boolean expressions that make up the larger
boolean expression. Firstly it checks for the lowercase ``a`` then if that is
false it will continue to the uppercase ``A`` check and if that is also false
then the entire boolean expression will be false and not execute the if
statements instructions. In python you can also use the ``and`` keyword if both
of these boolean expressions needed to be true in order to proceed. In this
case however the ``and`` keyword would do no good because a letter cannot be
lowercase and uppercase at the same time so we use ``or``.

Go with the flow man
--------------------

In programming we often use control flow statements to alter the way our code
performs. 

If your happy and you know it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For example if we want code to do one thing or another depending on a
variable we use an ``if`` statement. 

The if statement evaluates a boolean expression and executes the body of the if
statement if that boolean is positive. If however it is negative the code can
either; look for an else if and evaluate that expression next, look for an else
statement and do that instead of any condition, or finally continue normal
execution of the code.

In python we can give the following example that takes in a message code and
then prints the corresponding message:

.. doctest::

  >>> def message(code):
  ...     if code == 1:
  ...         print("Hello world!")
  ...     elif code == 2:
  ...         print("Goodbye cruel world!")
  ...     else:
  ...         print("I don't even know what to say...")
  ...     return True
  >>> message(1)
  Hello world!
  True
  >>> message(2)
  Goodbye cruel world!
  True
  >>> message(3)
  I don't even know what to say...
  True

Each part of an if statement is executed one after another until a positive
boolean expression is found. An ``else`` block is optional as is an ``else if``
(called ``elif`` in python) however if an ``else`` is used it must be last in
the chain as it acts as a sort of "catch all" in that if none of the if
statements are executed then the else surely will be.

Do a barrel roll!
~~~~~~~~~~~~~~~~~

Doing something over and over again until a particular time is done using loops
which are most commonly; ``for``, ``foreach``, and ``while``. In some cases
only one of the first two loops are available. In python there is a loop that
is started using the keyword ``for`` however it behaves like a ``foreach``
loop.

There are some minor but important differences between each loop type.

For
+++

Usually takes 3 statements; variable to count with, how to increment the
variable, and the condition in which to stop the for loop. In ``c/c++`` a for
loop would look something like this:

.. code-block:: c

  for (int count; count >= 10; count++){
      dosomething();
  }

This would, in order:

* create an integer variable called `count`.
* ensure the loop will stop when the number stored in `count` is greater then
  or equal to the number ``10``
* instruct the for loop to increase the number stored in `count` by 1 each
  loop.
* call the function ``dosomething`` with no arguments.

The body of the loop is the function call ``dosomething();``. The body of a
loop gets called until its end condition is met and the loop as played itself
out. Alternatively the body of a loop can tell the loop itself to ``break`` and
thus the loop will stop and return to executing the code outside of the loop.

Foreach
+++++++

A foreach loop typically wakes two statements. A iterable object and a name to
use for each element from that object. 

Firstly, an iterable is anything that has multiple elements to be retrieved or
iterated over. A list of names is iterable making a for loop the best way to
perform some action that uses each name on the list.

The following python code (python uses the ``for`` keyword even though it is
really behaves like a ``foreach``) will iterate over a list of friends names
and then call the ``print`` function with the current name until all names have
been iterated over.

.. doctest::

  >>> friends = ["nekroze", "lyshkah"]
  >>> for name in friends:
  ...     print(name)
  nekroze
  lyshkah

The ``foreach`` loop is a little bit of a newer concept then the ``for`` loop.
Many programmers would use a ``for`` loop that had an end condition be the
length of a list and just use the counter as an index to the list. This was
doing essentially the same thing as the ``foreach`` loop does but is much more
complicated. Python gets away with having only a ``foreach`` loop (using the
``for`` keyword however) because you can still get the original ``for`` loop
functionality by generating an iterable range for example, but many languages
have both.

While
+++++

The while loop takes only a condition and will keep looping until that
condition is met. A ``while`` loop is much like a ``for`` except it is up to
the programmer to create the counter variable and implement how it is
increased.

.. doctest::

  >>> loops = 0
  >>> while loops < 10:
  ...     loops += 1
  >>> loops
  10

An important thing to note, especially with ``while`` loops, is that the
condition can be any expression that can equate to a boolean. This can even be
a function so long as it returns something that can be considered a boolean.
