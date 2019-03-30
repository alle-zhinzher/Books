"""
Say you want to sort a list of numbers but prioritize one group of numbers to come first.
This pattern is useful when you’re rendering a user interface and want important messages
or exceptional events to be displayed before everything else.
A common way to do this is to pass a helper function as the key argument to a list’s
sort method. The helper’s return value will be used as the value for sorting each item in
the list. The helper can check whether the given item is in the important group and can
vary the sort key accordingly.
"""


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)
