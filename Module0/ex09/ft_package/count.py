def count_in_list(lst, element):
    """
    Counts how many times 'element' appears in 'lst'.
    Returns:
        int: The number of occurrences of 'element' in 'lst'.
    """
    element_count = 0
    for obj in lst:
        if obj == element:
            element_count += 1
    return element_count