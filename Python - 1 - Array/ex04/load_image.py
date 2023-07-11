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
        # image_array = np.array(image)
        #Cropping the image to have to correct size
        
        # cropped_image = image.crop((450, 100, 850, 500))
        # toto = np.array(image)
        # print(toto.shape)
        # image_array = np.array(cropped_image)
        # pouet = image_array[0:400, 0:400, 1]
        # print("The shape of pouet is: ", pouet.shape)
        # print(pouet)
        # print("The shape of image is: ", image_array.shape)
        # print(image_array[..., :, 0:1])
        # print("New Shape after Transpose: ", end="")
        # rotated_image = cropped_image.transpose(Image.ROTATE_90,)
        # image_array = np.array(rotated_image)
        # print(image_array.shape)
        # print(image_array)
        # rotated_image.show()
        
        
        
        
        cropped_image = image.crop((450, 100, 850, 500))
        toto = np.array(image)
        print(toto.shape)
        image_array = np.array(cropped_image)
        print("The shape of image is: ", image_array.shape)
        print(image_array[..., :, 0:1])
        print("New Shape after Transpose: ", end="")
        rotated_image = cropped_image.transpose(Image.ROTATE_90,)
        image_array = np.array(rotated_image)
        print(image_array.shape)
        print(image_array)
        # Display the zoomed image
        rotated_image.show()
    except AssertionError as e:
        print(e)



