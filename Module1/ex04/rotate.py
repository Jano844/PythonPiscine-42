
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from load_image import ft_load



def add_axies_and_save(img, save_path='output_with_axes.jpg'):
    """Take the Image, put axies on it and save it to the Path"""
    fig, ax = plt.subplots()

    if isinstance(img, Image.Image):
        img = np.array(img)

    if img.ndim == 3 and img.shape[-1] == 1:
        img = np.squeeze(img)

    ax.imshow(img, cmap='gray')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Image with Axes')
    plt.axis('on')
    plt.savefig(save_path)
    plt.close(fig)


def dreh_Bild(img):
    height, width = img.size

    print(height, width)

    transposed_img = Image.new("L", (height, width))

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            transposed_img.putpixel((y, x), pixel)

    return transposed_img


def zoom(path: str, zoom_factor: int):
    """Load The image Path, zoom into the picture and change it RGB values to Gray"""
    img = ft_load(path)

    print(f"The shape of image is: {img.shape}")
    print(img)

    height, width, _ = img.shape
    start_y = (height - zoom_factor) // 2 - 75 # -75 just to shift in y direction
    start_x = (width - zoom_factor) // 2 + 75 # shift in x dir
    sliced = img[start_y:start_y + zoom_factor, start_x:start_x + zoom_factor, 0]

    # Transpose Image


    #  Save the Image, cant Print it in the Terminal, because Docker lol
    output= dreh_Bild(Image.fromarray(sliced))
    add_axies_and_save(output)
    output.save("output.jpg")

    sliced = np.expand_dims(sliced, axis=-1)
    print(f"New shape after slicing: {sliced.shape}")
    np.set_printoptions(threshold=100, edgeitems=3, linewidth=120)
    print(sliced)

    return


if __name__ == "__main__":
    zoom("animal.jpeg", 400)