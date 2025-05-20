from PIL import Image
from load_image import ft_load
import numpy as np


def ft_invert(array):
    invert = 255 - array
    Image.fromarray(invert).save("pimped/invert.jpg")
    return invert

    
def ft_red(array):
    red = array * [1, 0, 0]
    red = red.astype(np.uint8)
    Image.fromarray(red).save("pimped/red.jpg")
    return red

    
def ft_green(array):
    green = array - array # Clear Array
    green[:, :, 1] = array[:, :, 1] # add Green Channel (; ; 1)
    Image.fromarray(green).save("pimped/green.jpg")
    return green

    
def ft_blue(array):
    blue = array.copy()
    blue[:, :, 0] = 0  # Red channel
    blue[:, :, 1] = 0  # Green channel
    Image.fromarray(blue).save("pimped/blue.jpg")
    return blue

    
def ft_grey(array):
    grey = array.copy()
    grey[:, :, 0] = grey[:, :, 1]
    grey[:, :, 2] = grey[:, :, 1]
    Image.fromarray(grey).save("pimped/grey.jpg")
    return grey


def main():
    array = ft_load("landscape.jpg")

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

if __name__ == "__main__":
    main()


