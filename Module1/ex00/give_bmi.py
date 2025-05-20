import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    h = np.square(height)
    w = np.array(weight)


    return list(map(float, w / h))

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi = np.array(bmi)

    return list(map(bool, bmi > limit))


if __name__ == "__main__":
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    print(give_bmi(height, weight))
