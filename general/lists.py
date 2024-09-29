mylyst = ["dog", "cat", "rat", "cow", "bug", "kid"]


def find_index(my_list, search_string):
    """Finds the index of the first occurrence of a given string in a list.

    Args:
        my_list: The list to search.
        search_string: The string to search for.

    Returns:
        The index of the first occurrence of the string in the list
        or -1 if the string is not found.
    """

    for i, item in enumerate(my_list):
        if item == search_string:
            return i
    return -1
