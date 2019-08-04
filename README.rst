KarelPy
=======

KarelPy is an education library written in Python to help beginners to
programming in general and Python learn to code by moving the robot
(Karel) and completing various challenges.


Inspiration for this project was gotten from the Karel tool used in
Stanford's `CS106A Programming
Methodology <https://www.youtube.com/watch?v=KkMDCCdjyW8&list=PL84A56BC7F4A1F852>`__
course taught by Sahami Mehran.


Installation
------------

Use the package manager `pip <https://pip.pypa.io/en/stable/>`__ to
install foobar.

.. code:: bash

    pip install karelpy

Objective
---------

The goal of the project is to help beginners to programming logic have a
feel of the workflow. Hopefully, beginners to Python can also use it as
a learning tool.

Learning will Karel should be interesting, as there will be various
challenges to be worked on and users will need to:

    **Create their own functions**: This is why the functionalities are limited,
    and users will need to create their own functions, combining the
    available methods.

    **Create loops**: A lot of tasks will be repetitive, so loops will come in
    handy.

    **Create conditionals**: Karel won't be allowed to crash into walls, pick
    beepers where they don't exist, so users will have to use conditionals
    before taking certain actions.

...and many more.

Usage
-----

Here's a code snippet:

.. code:: python

    from karelpy import karel

    karel.load(1)
    karel.move()
    karel.turn_left()
    karel.move()

    if karel.front_is_clear():
        karel.move()
    else:
        karel.turn_left()

    karel.move()
    karel.pick_beeper()
    karel.wait()

The snippet above will cause the robot to move, turn left, and move.


Code can be run as:

.. code:: bash

    python example.py

Here's a list of available methods:

Actions: - move - turn\_left - pick\_beeper - put\_beeper

Queries: - beepers\_present - beepers\_in\_bag - front\_is\_clear -
left\_is\_clear - right\_is\_clear - facing\_north - facing\_south -
facing\_east - facing\_west

Other methods:
~~~~~~~~~~~~~~

**display**

Displays the world to be worked in.

.. code:: python

    from karelpy import display

    display()

**load**

Loads the world to be worked in.

.. code:: python

    from karelpy import load

    load(2) # Loads the second world

**wait**

Prevents the world from closing immediately after runs to completion

.. code:: python

    from karelpy import karel, wait

    karel.move()
    karel.turn_left()
    karel.move()
    wait()

**close**

Closes the world to be worked in, and the window.

.. code:: python

    from karelpy import display, close

    display()
    close()

Contributing
------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Here's a couple of things on my mind:

-  Generation of random worlds
-  Accepting custom worlds from users
-  Addition of more worlds
-  A beeper count display
-  A beeper bag count display
-  Range of options for robot icons
-  Range of options for beeper icons
-  Refactoring

License
-------

`MIT <https://choosealicense.com/licenses/mit/>`__