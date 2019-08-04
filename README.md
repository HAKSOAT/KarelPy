# KarelPy

KarelPy is an education library written in Python to help beginners to
programming in general and Python learn to code by moving the robot
(Karel) and completing various challenges.

Inspiration for this project was gotten from the Karel tool used in
Stanford's [CS106A Programming
Methodology](https://www.youtube.com/watch?v=KkMDCCdjyW8&list=PL84A56BC7F4A1F852)
course taught by Sahami Mehran.

## Installation


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install
foobar.

```bash
pip install karelpy
```

## Objective


The goal of the project is to help beginners to programming logic have a
feel of the workflow. Hopefully, beginners to Python can also use it as
a learning tool.

Learning will Karel should be interesting, as there will be various
challenges to be worked on and users will need to:

> **Create their own functions**: This is why the functionalities are
> limited, and users will need to create their own functions, combining
> the available methods.
>
> **Create loops**: A lot of tasks will be repetitive, so loops will
> come in handy.
>
> **Create conditionals**: Karel won't be allowed to crash into walls,
> pick beepers where they don't exist, so users will have to use
> conditionals before taking certain actions.

...and many more.

## Demo

![Demo](demo.gif)


## Usage


Here's a code snippet with file name `example.py`:

```python
from karelpy import load, wait

karel = load(1)
karel.move()
karel.turn_left()
karel.move()

if karel.front_is_clear():
    karel.move()
else:
    karel.turn_left()

karel.move()
karel.pick_beeper()
wait()
```

Code can be run from CMD or Terminal as:

```bash
python example.py
```

Here's a list of available methods:

Actions:
- move 
- turn_left 
- pick_beeper 
- put_beeper

Queries:
- beepers_present
- beepers_in_bag 
- front_is_clear
- left_is_clear 
- right_is_clear 
- facing_north 
- facing_south
- facing_east 
- facing_west

### Other methods:

**display**

Displays the world to be worked in. Load should be called first, as you can't display a world without first loading it.

```python
from karelpy import display, load
karel = load(1)
display()
```

**load**

Loads the world to be worked in. Nothing can be done without loading the world first.

```python
from karelpy import load
karel = load(2) # Loads the second world
```

**wait**

Prevents the world from closing immediately after runs to completion.

```python
from karelpy import load, wait
karel = load(1) # Loads the first world
karel.move()
karel.turn_left()
karel.move()
wait()
```

**close**

Closes a window after displaying; should be used only if display is called in the interactive shell.

```bash
>>> from karelpy import close, display, load
>>> karel = load(1)
>>> display()
>>> close()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Here's a couple of things on my mind:

-   Generation of random worlds
-   Accepting custom worlds from users
-   Addition of more worlds
-   A beeper count display
-   A beeper bag count display
-   Range of options for robot icons
-   Range of options for beeper icons
-   Refactoring

## License

[BSD](https://choosealicense.com/licenses/bsd-2-clause/)
