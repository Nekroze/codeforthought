Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

You too can contribute to this book. As a matter of fact almost the entire
proccess is covered in **Code for Thought** itself.

The whole book is a relatively simple to use github repository at
https://github.com/Nekroze/codeforthought where it can easily be forked,
modified and "pull requested".

If you see a problem with this book; I said something ineloquently (probably
many things), Something was hard to understand or something just doesn't work
properly (it can happen! dont look at me like that).

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Is something not working the way the book says it does?

Report bugs at https://github.com/Nekroze/codeforthought/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

We can always explain something badly or word something poorly. Anyone is
welcome to help make **Code for Thought** more readable and understanable for
everyone.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/Nekroze/codeforthought/issues.

If you are proposing a feature:

* Explain in detail how it would work and why this it is better for everyone.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `codeforthought` for local development.

1. Fork the `codeforthought` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/codeforthought.git

3. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

4. When you're done making changes, check that your changes pass all the tests.
   You can use either the following command to do all tests at once::

    $ make test

   Or seperately:

   1) Test web links::

        $ make linkcheck

   2) Test doctests and code examples::

        $ make doctest

   3) Test html building::

        $ make html


5. Commit your changes and push your branch to GitHub::

    $ git add --all .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

6. Submit a pull request through the GitHub website.
