import time
from potions import make_potion


def print_delay_dots(dur=0.6, number=1):
    for i in range(number):
        time.sleep(dur)
        print('.')


def test_make_python_expert_potion():
    potion = make_potion.make_python_expert_potion(name='Boring Tester')

    target_potion = 'python_expert'
    container = 'pewter_cauldron'
    heat_source = 'fire'
    ingredients = ['fish_eyes', 'tea_leaves', 'unicorn_hair']
    cooked = True
    simmer_duration = 2

    print('-------------------------------')
    print(f'A sour looking Snape walks towards you to inspect your {target_potion} potion.')
    print(f'"What do we have here, {potion.name}...?"')
    print_delay_dots()

    # make the print statements work anyways, but actually unnecessary check
    if potion.container != container or potion.heat_source != heat_source:
        print(f'Snape smirks and remarks "You have used the wrong cauldron or heat, {potion.name}!" \n'
              f'With a flick of his wand he vanishes the potion. \n'
              f'"I am taking 10 points from Ravenclaw, {potion.name}. Start again!"')

    # check that correct setup was used
    assert potion.container == container
    assert potion.heat_source == heat_source
    print(f'You have used the correct setup, Snape cannot complain - he looks even more sour.')
    print_delay_dots()

    # make the print statements work anyways, but actually unnecessary check
    if sorted(potion.ingredients) != ingredients:
        print(f'Snape smirks and remarks "You have used the wrong ingredients, {potion.name}!" \n'
              f'With a flick of his wand he vanishes the potion. \n'
              f'"I am taking 10 points from Gryffindor, {potion.name}. Start again!"')

    # check if all ingredients are there
    assert sorted(potion.ingredients) == ingredients
    print(f'You have used the correct ingredients, Snape cannot complain - his face darkens.')
    print_delay_dots()

    # make the print statements work anyways, but actually unnecessary check
    if potion.cooked != cooked or potion.simmer_duration != simmer_duration:
        print(f'Snape smirks and remarks "Your potion is not properly cooked!" \n'
              f'With a flick of his wand he vanishes the potion. \n'
              f'"I am taking 10 points from Hufflepuff, {potion.name}. Start again!"')

    # check that potion is cooked
    assert potion.cooked == cooked
    assert potion.simmer_duration == simmer_duration
    print(f'The potion is cooked properly, Snape cannot complain - he is looking annyoyed now.')
    print_delay_dots()

    print(f'Snape mutters "You got away this time, {potion.name}!", since there is nothing wrong with '
          f'your {target_potion} potion. \n \n'
          f'You pack your bags and leave as fast as you can to have a butterbeer at the lake!')
    return
