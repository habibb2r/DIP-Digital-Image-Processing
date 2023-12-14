# -*- coding: utf-8 -*-
"""DIPLABFinal-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11h0mjekdXvUNUBHR9y3fr7lL0I_uc1lV
"""

#Write generic functions for each of the following.
# -> Takes input mask size and their numeric values from the user and create the mask
# -> Take image and padding size as argument and add padding on the image (either zeros or copy neighboring pixel)
# -> Take image and filter as argument and apply the filter to the image
# -> Take image as input and normalize the image between 0 - 255

import numpy as np
import cv2
print("OpenCV-Python Version {}".format(cv2.__version__))
from skimage import io
import matplotlib.pyplot as plt


image = io.imread('https://media.wired.com/photos/593261cab8eb31692072f129/master/pass/85120553.jpg')
plt.imshow(image)
plt.show()

import numpy as np
import cv2
from skimage import io
import matplotlib.pyplot as plt


# Load the image
image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/575px-Cat_November_2010-1a.jpg'
image = io.imread(image_url)
plt.imshow(image)
plt.show()
# Task 1: Create Mask Function


padding_size = 50
padding_color = (128, 0, 128)



def create_mask(mask_size):
    mask = np.zeros((mask_size, mask_size), dtype=np.uint8)
    for i in range(mask_size):
        for j in range(mask_size):
            mask[i , j] = int(input(f"Enter value for mask[{i}][{j}]: "))
    return mask


def add_padding(image, padding_size, padding_color):
    padded_image = cv2.copyMakeBorder(image, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_CONSTANT, value=padding_color)
    return padded_image


def apply_filter(image, filter):
    filtered_image = cv2.filter2D(image, -1, filter)
    return filtered_image

# Task 4: Normalize Image Function
def normalize_image(image):
    min_val = np.min(image)
    max_val = np.max(image)
    normalized_image = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return normalized_image


# Apply padding

padded_image = add_padding(image, padding_size, padding_color)
plt.figure(figsize=(10,10))

# Apply filter (you would need to define a filter kernel)

filter_kernel = np.array([[-1, -2, -1], [0, 1, 0], [1, 2, 1]]) / 9
filtered_image = apply_filter(padded_image, filter_kernel)
# Normalize image
normalized_image = normalize_image(filtered_image)
# Display the results
plt.subplot(1, 2, 1)
plt.title('Filtered Image E')
plt.imshow(normalized_image)
plt.show()



filter_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]) / 9
filtered_image = apply_filter(padded_image, filter_kernel)
# Normalize image
normalized_image = normalize_image(filtered_image)
# Display the results
plt.subplot(1, 2, 2)
plt.title('Filtered Image C')
plt.imshow(normalized_image)
plt.show()


filter_kernel = np.array([[-1, -2, -1],
                          [0,  0, 0],
                          [1, 2, 1]]) / 9
filtered_image = apply_filter(padded_image, filter_kernel)

normalized_image = normalize_image(filtered_image)

plt.title('Filtered Image D')
plt.imshow(normalized_image)
plt.show()


filter_kernel = np.array([[1, 1 , 1, 1, 1],
                          [1, 1 , 1, 1, 1],
                          [1, 1 , 1, 1, 1],
                          [1, 1 , 1, 1, 1],
                          [1, 1 , 1, 1, 1]]) / 25
filtered_image = apply_filter(padded_image, filter_kernel)

normalized_image = normalize_image(filtered_image)

plt.title('Filtered Image B')
plt.imshow(normalized_image)
plt.show()

import numpy as np
import cv2
from skimage import io
import matplotlib.pyplot as plt

# Load the image
image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/575px-Cat_November_2010-1a.jpg'
image = io.imread(image_url)
plt.imshow(image)
plt.show()

# Function to add padding to an image with a specific color
def add_padding_with_color(image, padding_size, padding_color):
    padded_image = cv2.copyMakeBorder(image, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_CONSTANT, value=padding_color)
    return padded_image

# Define the padding size and color (e.g., white color)
padding_size = 50
padding_color = (255, 255, 255)  # White color (RGB)

# Add padding with the specified color to the image
padded_image = add_padding_with_color(image, padding_size, padding_color)

# Display the padded image
plt.imshow(padded_image)
plt.show()