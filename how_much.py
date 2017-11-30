# If you get a recursion depth error, you could either increase the recursion depth
# (see: https://stackoverflow.com/questions/5061582/setting-stacksize-in-a-python-script/16248113#16248113)
# Or rewrite the code to be iterative.
#
# Note that increasing the recursion depth can be dangerous (mainly due to Python crashing, see below for more details),
# but the standard limit is a little bit conservative.
# (a copy pasta from the SO link above, works fine for example (on my machine)).
#
# The recursion depth is set as a guard to prevent infinite recursions from causing an overflow of the C stack
# and thus crashing Python (this is the 'dangerous' part)
# see: https://docs.python.org/3/library/sys.html#sys.setrecursionlimit
multiplication_factor = 100


class Tree(object):
    def __init__(self, lower_bound, upper_bound, cup=None, parent=None):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.cup = cup
        self.parent = parent

    def get_cups(self):
        """
        This method returns all the cups from the current node respecting all the cups
        that were set in it's parents (so it will return a list containing all the cups
        that were set up until (including) this node).

        :return: A list containing all the set cups up until (including) this node.
        """
        if self.cup is None:
            return []

        cups = [self.cup]

        if self.parent:
            cups = cups + self.parent.get_cups()

        return cups


def get_possible_sizes():
    # We need to multiply our sizes by 100 to prevent floating point issues whenever
    # we are doing the calculations.
    # This means that we need to multiply our input by 100 as well (and the +1 liter becomes
    # +100 liter, but that doesn't matter since everything got multiplied by 100)
    return [int(x * multiplication_factor) for x in [50, 35, .33, .3]]


def calculate_possible_combinations(cups, lower_bound, upper_bound):
    root = Tree(lower_bound, upper_bound)

    possible_combinations = add_nodes(root, cups)

    print("A total of {0} combinations are possible.".format(possible_combinations))


def add_nodes(tree, cups):
    possible_combinations = 0

    for cup in cups:
        if cup <= tree.upper_bound:
            child = Tree((tree.lower_bound - cup), (tree.upper_bound - cup), cup, tree)

            # Because we were allowed to have an additional of 1 liter (so valid combinations are between
            # our target and our target + 1) the upper bound value of our child node is a valid leaf node
            # if it's between the 0 and 1 (respecting our multiplication factor)
            # If this is the case, we got a valid combination
            if 0 <= child.upper_bound <= (1 * multiplication_factor):
                possible_combinations += 1
            else:
                # We only need to add nodes for all the cups that are equal to or lower
                # then the current cup, thus we will create a new list (`new_cups`) that
                # only contains values equal or lower to the current cup.
                # This because (5, 3, 2) is the same as (3, 5, 2) in the case
                # of storage. Thus we only need to check paths with decreasing numbers.
                new_cups = [c for c in cups if c <= cup]

                possible_combinations += add_nodes(child, new_cups)

    return possible_combinations


if __name__ == "__main__":
    user_input = input("How much beer do you need to order?")
    # See the PyDoc in get_possible_sizes() for the reasoning behind the `* 100`
    amount_of_beer_to_order = int(user_input) * multiplication_factor

    cups = get_possible_sizes()
    lower_bound = amount_of_beer_to_order
    upper_bound = amount_of_beer_to_order + (1 * multiplication_factor)

    calculate_possible_combinations(cups, lower_bound, upper_bound)
