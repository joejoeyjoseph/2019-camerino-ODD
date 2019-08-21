## Exercise: Importing

For these exercises to work, you have to either:

- work in the ODD_dir directory exclusively
- make your package available from anywhere by running `pip install -e .`(when in /ODD_dir) or `pip install -e /path/to/ODD_dir`from anywhere.

------

### Part 1 - importing potions from directories (repetition)

- Check that both `__init__.py` files are empty apart from the print statements. 

- In a terminal, navigate to the `ODD_dir` folder. Load a Python interpreter (type `$ python`) and run

  ```python
  >>> import potions
  ```

  - Can you access the class `Potion`in `potion.py` without another import statement?
  - If not, what do you have to import to access `Potion`?
  - Can you access the variable `fish_eyes`in `/tools/ingredients.py` without another import statement?
  - If not, what do you have to import to access `fish_eyes`?

Tip:

Make sure you quit and reload the Python interpreter whenever you change need to re-run import statements



------

### Part 2 - adding to the `potions/__init__.py` file to access a module in `/potions`

- What do you have to add to the `/potions/__init__.py`file so that the following statements work  (leave the `/potions/tools/__init__.py`file empty)?

  ```python
  >>> import potions
  >>> potions.potion.Potion()
  ```

  ```python
  >>> import potions
  >>> potions.Potion()
  ```

  ```python
  >>> import potions
  >>> Potion()
  ```

Tip:

Make sure you quit and reload the Python interpreter whenever you changed the `__init__.py`file.

Make sure you saved the changes in the `__init__.py`file.

Make sure you are editing the correct `__init__.py`file.

Remember that you can also import using `from <package_name> import <module_name>` and `from <module_name> import <function_name>`



------

### Part 3 - adding to the `potions/__init__.py` file to access a module in `/potions/tools`

- How can you access the variable fish_eyes if you import potions in a Python interpreter and `the /potions/__init__.py` file contains the following import statements:

  ```python
  from potions.tools import ingredients
  ```
  
a) potions.tools.ingredients.fish_eyes
  
  b) potions.tools.fish_eyes
  
  c) potions.ingredients.fish_eyes

  d) potions.fish_eyes
  
  ```python
  from potions.tools.ingredients import fish_eyes
```
  
  a) potions.tools.ingredients.fish_eyes
  
  b) potions.tools.fish_eyes
  
  c) potions.ingredients.fish_eyes
  
  d) potions.fish_eyes

Tip:

Try it out for yourself



------

### Part 4 - can you split statements over the two **init**.py files?

- You maybe noticed that in Part 3 you could not get `potions.tools.fish_eyes` to work (spoilers :) !).  
What import statements in the `/potions/tools/__init__.py` and`/potions/__init__.py` files do you need to get this to work? 
  
  ```python
  >>> import potions
  >>> potions.tools.fish_eyes
```
  
  
  
  

