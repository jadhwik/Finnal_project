//to save the model

gen.save('pix2pix.h5')


import tensorflow as tf
from PIL import Image
import numpy as np

# Define preprocessing functions
def normalize(input_image):
    input_image = (input_image / 127.5) - 1
    return input_image

def resize(input_image, image_size):
    input_image = tf.image.resize(input_image, [image_size, image_size], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    return input_image

# Define the load function with adjusted input shape
def load(image_file):
    image = tf.io.read_file(image_file)
    image = tf.image.decode_jpeg(image, channels=1)  # Adjust channels to 1
    input_image = tf.image.grayscale_to_rgb(image)  # Convert grayscale to RGB
    input_image = tf.cast(input_image, tf.float32)
    return input_image

# Load the trained model
loaded_model = tf.keras.models.load_model('pix2.h5')
image_size = 256  # Set the desired image size

# Load and preprocess the input image
path = 'dataset/dress_sketch/100.jpg'
input_image = load(path)  # Use the load function to load the image
input_image = resize(input_image, image_size)  # Resize the input image
input_image = normalize(input_image)  # Normalize pixel values to [-1, 1]
input_image = np.expand_dims(input_image, axis=0)  # Add batch dimension

# Obtain predictions for the input image
predictions = loaded_model.predict(input_image)

# Postprocess output (if needed)
# For example, if pixel values are in range [-1, 1], rescale them back to [0, 255]
output_image = ((predictions[0] + 1) * 127.5).astype(np.uint8)

# Save or visualize the output image
output_image = Image.fromarray(output_image.squeeze())
output_image.save('generated_image2.jpg')
output_image.show()
