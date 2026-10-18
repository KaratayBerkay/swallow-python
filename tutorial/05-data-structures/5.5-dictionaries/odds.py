odds = {i: i**2 for i in (1, 3, 5)}
evens = {i: i**2 for i in (2, 4, 6)}
{**odds, **evens}
all_values = [odds, evens, {0: 0}]
eval("{**i for i in all_values}")
