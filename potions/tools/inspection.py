"""This file contains the function for Snape checking your potion.

There is a docstring available for the function inspection_by_Snape.

In case you are wondering, this is the text in the module docstring of /tools/inspection.py .
"""
import time


def print_delay_dots(dur=0.6, number=1):
    for i in range(number):
        time.sleep(dur)
        print('.')


def inspection_by_Snape(potion, target_potion='python_expert'):
    """Checks if potion was brewed correctly.

    Prints narration of inspection process - read to see if potion passed inspection.
    Snape checks container, heat_source, ingredients, and whether potion was cooked.
    If something is wrong, function returns at that point.

    Parameters
    ----------
    potion : obj 
        Instance of Potion (class from potion_class).
    target_potion: str, optional
        Name of potion to be checked by Snape. Currently possible potions are 'python expert', 'example_potion'
    """

    print('-------------------------------')
    print(f'A sour looking Snape walks towards you to inspect your {target_potion} potion.')
    print(f'"What do we have here, {potion.name}...?"')
    print_delay_dots()

    # set variables for each potion that need to be checked
    if target_potion == 'python_expert':
        container = 'pewter_cauldron'
        heat_source = 'fire'
        ingredients = ['fish_eyes', 'tea_leaves', 'unicorn_hair']
        cooked = True
        simmer_duration = 2
    elif target_potion == 'example_potion':
        container = 'old_kettle'
        heat_source = 'eternal_flame'
        ingredients = ['fish_eyes', 'snake_skin']
        cooked = True
        simmer_duration = 5
    else:
        print(f'Target potion was not recognised, please check spelling.')

    # check that correct setup was used
    if potion.container == container and potion.heat_source == heat_source:
        print(f'You have used the correct setup, Snape cannot complain - he looks even more sour.')
    else:
        print(f'Snape smirks and remarks "You have used the wrong cauldron or heat, {potion.name}!" \n'
              f'With a flick of his wand he vanishes the potion. \n'
              f'"I am taking 10 points from Ravenclaw, {potion.name}. Start again!"')

    print_delay_dots()

    # check if all ingredients are there
    if sorted(potion.ingredients) == ingredients:
        print(f'You have used the correct ingredients, Snape cannot complain - his face darkens.')
    else:
        print(f'Snape smirks and remarks "You have used the wrong ingredients, {potion.name}!" \n'
              f'With a flick of his wand he vanishes the potion. \n'
              f'"I am taking 10 points from Gryffindor, {potion.name}. Start again!"')

    print_delay_dots()

    # check that potion is cooked
    if potion.cooked == cooked and potion.simmer_duration == simmer_duration:
        print(f'The potion is cooked properly, Snape cannot complain - he is looking annyoyed now.')
    else:
        print(f'Snape smirks and remarks "Your potion is not properly cooked!" \n'
              f'With a flick of his wand he vanishes the potion. \n'
              f'"I am taking 10 points from Hufflepuff, {potion.name}. Start again!"')

    print_delay_dots()

    print(f'Snape mutters "You got away this time, {potion.name}!", since there is nothing wrong with '
          f'your {target_potion} potion. \n \n'
          f'You pack your bags and leave as fast as you can to have a butterbeer at the lake!')

    return

