# Too Much?
# This was the most tricky one. We will explain how you could have resolved this.
# Lets start with that it was impossible to solve this within two hours.
# Even if you use a quite advanced algorithm like a tree, it takes hours to calculate all the options.
# To win the points you had to be able to detect this, and have provided us with proof that it worked on for example 20
# liters. We could check your code and run it with 10 liters to see if it matches our result.
# The numbers given as `input` were way too big. Hence the title "Too Much?"

## How to solve a problem like this?

### Bruteforce
# Using some libs (e.g. https://docs.python.org/3/library/itertools.html)
# you could have generated all the possible combinations.
# So lets say you have 250 liters as input, you can use 0-5 as a range for the 50 liter keg,
# and 0-7 for the 35 liter keg (in the case of `itertools.product()`).
# Then you generate a list of all the combinations of 50 and 35 liter kegs by looping
# through them. Whilst you create them, you can test every combination and see if it is between the 250 and 251 liters
# (remember, you can be one liter over).

### A little bit smarter
# Using a Tree pattern you can add a node for every valid combination.
# By forming a tree you prevent
# A: double data,
# B: a huge dataset.
# When using bounds in a smart way you only add "nodes" that are actually possible.
# In the end you only have to count the nodes to get the amount of combinations you can make.
# And loop through the generated nodes to create a list of options.
# Below we have provided a basic setup with the tree pattern.
possible_combinations = 0
multiplication_factor = 100


class Tree(object):
    def __init__(self, lower_bound, upper_bound, parent = None):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.parent = parent


def get_possible_sizes():
    # We need to multiply our sizes by 100 to prevent floating point issues whenever
    # we are doing the calculations.
    # This means that we need to multiply our input by 100 as well (and the +1 liter becomes
    # +100 liter, but that doesn't matter since everything got multiplied by 100)
    return [int(x * multiplication_factor) for x in [50, 35, .33, .3]]


def calculate_possible_combinations(cups, lower_bound, upper_bound):
    root = Tree(lower_bound, upper_bound)

    add_nodes(root, cups)

    print("A total of {0} combinations are possible.".format(possible_combinations))


def add_nodes(tree, cups):
    for cup in cups:
        if cup <= tree.upper_bound:
            child = Tree((tree.lower_bound - cup), (tree.upper_bound - cup), tree)

            # Because we were allowed to have an additional of 1 liter (so valid combinations are between
            # our target and our target + 1) the upper bound value of our child node is a valid leaf node
            # if it's between the 0 and 1 (respecting our multiplication factor)
            # If this is the case, we got a valid combination
            if 0 <= child.upper_bound <= (1 * multiplication_factor):
                # Using global variables is not really nice, but it's super convenient
                # in the context of this script, and since it's a one time thing, it's
                # kinda redeemable to use it.
                global possible_combinations
                possible_combinations += 1
            else:
                add_nodes(child, cups)

    return tree


if __name__ == "__main__":
    user_input = input("How much beer do you need to order?")
    # See the PyDoc in get_possible_sizes() for the reasoning behind the `* 100`
    amount_of_beer_to_order = int(user_input) * multiplication_factor

    cups = get_possible_sizes()
    lower_bound = amount_of_beer_to_order
    upper_bound = amount_of_beer_to_order + (1 * multiplication_factor)

    calculate_possible_combinations(cups, lower_bound, upper_bound)
