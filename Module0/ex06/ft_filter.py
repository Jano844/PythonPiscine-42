import sys
from filterstring import is_longer_than_n as func


def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable-
    for which function(item) is true.
    If the Function is None, filter will yield all items that are true
    Yield is used to 'save' the Items
    """

    if function is None:
        for item in iterable:
            if item:
                yield item
    else:
        for item in iterable:
            if function(item):
                yield item


def is_even(n):
    """Returns true if even"""
    return n % 2 == 0


def main():
    """
    Checks the user Input
    Prints the result
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    string_arg = sys.argv[1]

    try:
        n = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    result = list(ft_filter(lambda word: func(word, n), string_arg.split()))
    print(result)

    data = [0, 1, 2, 3, 4, 5]
    print(list(ft_filter(is_even, data)))


if __name__ == "__main__":
    main()
