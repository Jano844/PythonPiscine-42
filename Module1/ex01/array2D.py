import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    arr = family

    shape = np.shape(arr)
    slice_pattern = slice(start, end)
    sliced_shape = np.shape(arr[slice_pattern])

    print(shape)
    print(sliced_shape)

    return arr[slice_pattern]



if __name__ == "__main__":
    family = [[1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))