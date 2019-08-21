"""This file contains all defined cooking methods for brewing potions.

All cooking methods are functions, so there are docstrings available.

In case you are wondering, this is the text in the module docstring of /tools/cooking.py .
"""


dummy = 1


def stir(potion, direction):
    """Stirs the potion.

    Updates colour in the class instance.

    Parameters
    ----------
    potion : Potion instance
        The potion to be stirred.
    direction : {'clockwise', 'anti-clockwise'} str
        The direction in which the potions is to be stirred
    """
    if direction == "clockwise":
        potion.colour = "vomit-yellow"
        print('NO!! Your potion turns vomit-yellow. Did you stir in the right direction?')
        return
    if direction == "anti-clockwise":
        potion.colour = "newt-green"
        print('Your potion turns a lovely newt-green.')
        return


def simmer(potion, duration):
    """Cooks the potion.

    Updates simmer_duration and cooked attributes in the class instance.

    Parameters
    ----------
    potion : Potion instance
        The potion to be cooked.
    duration : int
        How long to cook the potion for [hours].
    """
    potion.simmer_duration = duration
    if duration < 2:
        print('Are you sure you are cooking the potion enough? Your ingredients look a bit raw...')
    elif duration > 5:
        print('Oops, you have fallen asleep at your desk! Are you sure you want to simmer this long?')
    else:
        potion.cooked = True
    return


