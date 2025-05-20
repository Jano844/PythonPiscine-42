from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    img = Image.open(path).convert("RGB")
    data = np.array(img)

    return data


if __name__ == "__main__":
    ft_load("")