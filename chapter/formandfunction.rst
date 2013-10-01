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
called as well as optionally asking for a input data and possibly providing an
output.

Imagine we had a reason to count how many times the letter "``a``" is in a
given string and return that result. Instead of writing the instructions
required to perform this task each time it is needed in our code we could just
write a function that does it for us. For example in python we would do the
following:

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
``a`` we could change the if statement a little to look like the following::

.. code-block:: python

  if letter == "a" or letter == "A":

Then the if statement has two boolean expressions that make up the larger
boolean expression. Firstly it checks for the lowercase ``a`` then if that is
false it will continue to the uppercase ``A`` check and if that is also false
then the entire boolean expression will be false and not execute the if
statements instructions. In python you can also use the ``and`` keyword if both
of these boolean expressions needed to be true in order to proceed. In this
case however the ``and`` keyword would do no good because a letter cannot be
lowercase and uppercase at the same time so we use ``or``.
