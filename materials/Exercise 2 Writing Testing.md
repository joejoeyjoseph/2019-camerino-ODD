## Exercise: Writing and testing functions

We want to mimic the *write function*⇄ *test function* workflow. This is supposed to be easy and fun, so feel free to make mistakes with the potion and test as much as you want.

Write a function that makes the Python expert potion (instructions below). Test it either as shown with the example potion in `make_potion.py` or with pytest.

### Brewing instructions

Make a new potion called 'python_expert' according to these instructions:

```
- Set up a pewter cauldron and light a fire underneath it.
- Add fish eyes, unicorn hair and tea leaves and stir anti-clockwise.
- Let simmer for 2 hours (should turn from transparent to green).
- Have Snape inspect the potion (use target_potion='python_expert').
```

You can check the colour as you go to see if it is progressing well via the Potion method `check_colour`.
Note that the `example_potion()`function is missing a crucial step and does not pass Snape's inspection. You can find more information by accessing the documentation of `Potion()`using `help(potions.potion.Potion)`.

### Tests

We have written two tests for your function:

- the unofficial one is the funnier one with print statements: the `inspection_by_Snape()`function in the `/tools/inspection.py`module.
  To use it, you call the function as shown in the example potion in `make_potion.py`.
- the official one is `/ODD_dir/tests/test_make_potion.py`, which you can call (as you should know from your lecture with Pietro) with `$ pytest test_make_potion.py`. This will not display any funny If you want the print statements, use `$ pytest test_make_potion.py -s`, if you don't care about the 

Note that if you call inspection_by_Snape, you should never get an error, so you will have to read what Snape does and says to find out what went wrong.



Feel free to use either, but we recommend the unofficial one :) - but only in this instance!

### Help

You may change the import statements to anything more comfortable.

You can access the documentation for any function you use via the help function: `help(package_name.module_name.class_name.method_name)`. If you have changed your import statements to use `Potions()`directly, you can also access its documentation in that way i.e. `help(Potions)`.

(Press `q`to exit the help)

You also may look into the files in `/potions`and `/tools`
