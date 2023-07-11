import array
import os
import sys
import numpy as np
from PIL import Image

sys.tracebacklimit = 0


def load_image() -> array:
    try:
        # Get the current working directory
        current_dir = os.getcwd()
        # Image file path
        image_path = os.path.join(current_dir, "animal.jpeg")
        # Open the image
        image = Image.open(image_path)
        image_array = np.array(image)
        print("The shape of image is: ", image_array.shape)
        print(image_array[0])
        #Cropping the image to have to correct size
        cropped_image = image.crop((450, 100, 850, 500))
        # Calculate the new size based on the zoom factor
        # width, height = cropped_image.size
        # new_width = int(width * 2)
        # new_height = int(height * 2)
        # Resize the image using the new size
        # resized_image = cropped_image.resize((new_width, new_height))
        # resized_array = np.array(resized_image)
        # print(cropped_image.frombytes)
        resized_array = np.array(cropped_image)
        print("New Shape after slicing: ", end="")
        print(resized_array.shape)
        sliced = resized_array[..., :, 0:1]
        print(sliced)
        # Display the zoomed image
        cropped_image.show()
    except AssertionError as e:
        print(e)



