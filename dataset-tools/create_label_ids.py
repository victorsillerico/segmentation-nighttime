import cv2
import numpy as np
import pandas as pd
import os

# Path directory for mask in RGB 
mask_dir_path = '/home/vhsillerico/Documents/datasets/carla-night/Town02/color-masks'

# Path directory to save masks with IDs
mask_with_ids_path = '/home/vhsillerico/Documents/datasets/carla-night/Town02/labelIds'

# Path of CSV file with information of class name, RGB values
class_dict = pd.read_csv('/home/vhsillerico/Documents/datasets/carla-night/label_class_dict_carla.csv')

# Initialize an empty dictionary for color to label mapping
color_to_label_mapping = {}

# Iterate over the DataFrame rows (excluding the header)
for index, row in class_dict.iterrows():
    # Extract the RGB values and convert them to integers
    r, g, b = int(row['# r']), int(row['# g']), int(row['# b'])
    # Create the color tuple
    color = (r, g, b)
    # Add the color tuple to the dictionary with the current index as the value
    color_to_label_mapping[index] = color

# Convert RGB values to a label code value (0 to 33)
def color_to_ids(color_mask, color_to_label_mapping):
    # Convert the RGB image to a NumPy array
    mask_arr = np.array(color_mask)

    # Create an empty array for encoded labels
    mask_ids = np.zeros((mask_arr.shape[0], mask_arr.shape[1]), dtype=np.float32)

    # Replace colors with one-hot labels
    for label_id, color in color_to_label_mapping.items():
        mask = np.all(mask_arr == np.array(color), axis=-1)
        mask_ids[mask] = label_id

    return mask_ids

# Create the output directory if it does not exist
os.makedirs(mask_with_ids_path, exist_ok=True)

# Process each image in the mask directory
for filename in os.listdir(mask_dir_path):
    if filename.endswith('.png'):
        # Construct full file path
        mask_file_path = os.path.join(mask_dir_path, filename)
        
        # Read the RGB mask image
        #rgb_mask = cv2.imread(mask_file_path, cv2.IMREAD_COLOR)
        rgb_mask = cv2.cvtColor(cv2.imread(mask_file_path), cv2.COLOR_BGR2RGB)
        
        # Convert RGB to label IDs
        mask_with_ids = color_to_ids(rgb_mask, color_to_label_mapping)
        
        # Convert mask_with_ids to uint8 (0-33) and then save it as PNG
        mask_uint8 = mask_with_ids.astype(np.uint8)
        
        # Save the new mask_with_ids as a PNG image
        output_file_path = os.path.join(mask_with_ids_path, filename)
        cv2.imwrite(output_file_path, mask_uint8)

        print(f"Processed and saved {filename} to {output_file_path}")
