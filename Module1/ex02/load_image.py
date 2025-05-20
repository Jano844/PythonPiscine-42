from PIL import Image
import numpy as np



def ft_load(path: str) -> np.ndarray:
    img = Image.open(path).convert("RGB")
    data = np.array(img)

    # print(f"The Shape of images is: {data.shape}")
    return data



if __name__ == "__main__":
    ft_load("")