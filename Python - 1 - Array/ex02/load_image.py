import array
import os
import sys
import numpy as np
from PIL import Image

sys.tracebacklimit = 0

# Display information about the image


def ft_load(path: str) -> array:
    """Load an image from the str name and
    display the informations
    """
    assert isinstance(path, str), "The argument must be a string"
    try:
        # Get the current working directory
        current_dir = os.getcwd()
        # Image file path
        image_path = os.path.join(current_dir, path)
        # Open the image
        image = Image.open(image_path)
        image_array = np.array(image)
        print("The shape of image is: ", image_array.shape)
    except AssertionError as e:
        print(e)
    return image_array
