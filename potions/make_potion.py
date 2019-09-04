import potions.potion
import potions.tools.equipment
import potions.tools.ingredients
import potions.tools.cooking
import potions.tools.inspection


def make_example_potion(name):

    my_potion = potions.potion.Potion(name=name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=potions.tools.equipment.old_kettle, heat_source=potions.tools.equipment.eternal_flame)
    # Simmer for 5 hours.
    potions.tools.cooking.simmer(my_potion, duration=5)

    return my_potion

""" This function makes expert potions."""

def make_python_expert_potion(name):
    """
    Set up equipment, ingredients, stirring and cooking.

    In this function you specify the above mentioned settings and therefore, create your expert potion.

    Parameters
    -----------
    name: str
        Name of your potion.
    
    Returns
    -----------
    python_potion - obj
    """
    python_potion = potions.potion.Potion(name=name)
    # Set up
    python_potion.setup(container=potions.tools.equipment.pewter_cauldron, heat_source=potions.tools.equipment.fire)
    # Add ingredients
    python_potion.add_ingredients(ingredients=[potions.tools.ingredients.fish_eyes, potions.tools.ingredients.unicorn_hair, potions.tools.ingredients.tea_leaves])
    # Stir
    potions.tools.cooking.stir(python_potion, 'anti-clockwise')
    # Simmer
    potions.tools.cooking.simmer(python_potion, duration=2)
    
    return python_potion


if __name__ == '__main__':

#    my_name = 'Potter'
#    my_potion = make_example_potion(name=my_name)
    # Let Snape inspect the potion
#    potions.tools.inspection.inspection_by_Snape(potion=my_potion, target_potion='example_potion')

    python_name = 'python_expert'
    python_potion = make_python_expert_potion(name=python_name)
    # Inspect
    potions.tools.inspection.inspection_by_Snape(potion=python_potion, target_potion='python_expert')