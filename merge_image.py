from PIL import Image
import os

# Base directory path
base_path_images = r'C:\Users\91984\Desktop\my_projects\.ipynb_checkpoints\dataset\dress_images'
base_path_sketch = r'C:\Users\91984\Desktop\my_projects\.ipynb_checkpoints\dataset\dress_sketch'

# Output directory path
output_path = r'C:\Users\91984\Desktop\my_projects\.ipynb_checkpoints\dataset\merged_images'

# Number of images to merge
num_images = 3000  # Change this to the desired number

# Iterate over the range of images
for i in range(1, num_images + 1):
    # Construct file paths for images
    image_path = os.path.join(base_path_images, f'{i}.jpg')
    sketch_path = os.path.join(base_path_sketch, f'{i}.jpg')

    # Create a list to store opened images
    images = [Image.open(image_path), Image.open(sketch_path)]

    # Calculate the total width and height for the new image
    total_width = sum(img.width for img in images)
    max_height = max(img.height for img in images)

    # Create a new image with the calculated dimensions
    image_new = Image.new('RGB', (total_width, max_height))

    # Paste each image onto the new image
    current_width = 0
    for img in images:
        image_new.paste(img, (current_width, 0))
        current_width += img.width

    # Save the merged image with a distinct name
    output_file_path = os.path.join(output_path, f'merged_image_{i}.png')
    image_new.save(output_file_path)
