import array
import os
import sys
import numpy as np
from PIL import Image
from load_image import ft_load


def ft_invert(array) -> array:
    """Invert the colors of the image received."""
    inverted_image = Image.eval(array, lambda pixel: 255 - pixel)
    inverted_image.show()

def ft_red(array) -> array:
    """
    Put the colors of the image received in red
    The green and blue channels are set to 0 using the - operator.
    """
    red_image = array.copy()
    # Get the pixel data of the image
    pixels = red_image.load()
    # Iterate over each pixel
    for y in range(red_image.size[1]):
        for x in range(red_image.size[0]):
            r, g, b = pixels[x, y]
            # Set the red channel value to its original value
            # and set green and blue channels to 0
            pixels[x, y] = (r, 0, 0)
    red_image.show()


def ft_green(array) -> array:
    """
    Put the colors of the image received in green
    The red and blue channels are set to 0 using the - operator.
    """
    green_image = array.copy()
    # Get the pixel data of the image
    pixels = green_image.load()
    # Iterate over each pixel and set red and blue channels to 0
    for y in range(green_image.size[1]):
        for x in range(green_image.size[0]):
            _, g, _ = pixels[x, y]
            pixels[x, y] = (0, g, 0)
    green_image.show()



def ft_blue(array) -> array:
    """Put the colors of the image received in green
    The red and green channels are set to 0 using the - operator.
    """
    green_image = array.copy()
    # Get the pixel data of the image
    pixels = green_image.load()
    # Iterate over each pixel and set red and blue channels to 0
    for y in range(green_image.size[1]):
        for x in range(green_image.size[0]):
            _, _, b = pixels[x, y]
            pixels[x, y] = (0, 0, b)
    green_image.show()

def ft_grey(array) -> array:
    """Put the colors of the image received in grey
    Transform the image to grayscale using = and / operators.
    In this version, we calculate the average pixel value (avg)
    by summing the red, green, and blue channel values
    and then dividing it by 3 using the / operator.
    We assign the avg value to each channel to achieve the grayscale effect.
    """
    gray_image = array.copy()
    # Get the pixel data of the image
    pixels = gray_image.load()
    # Iterate over each pixel and set each channel value to the average
    for y in range(gray_image.size[1]):
        for x in range(gray_image.size[0]):
            r, g, b = pixels[x, y]
            avg = (r + g + b) // 3
            pixels[x, y] = (avg, avg, avg)
    gray_image.show()
