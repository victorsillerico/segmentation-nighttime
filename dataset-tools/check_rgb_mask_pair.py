import os

def check_images_in_directories(dir_A, dir_B):
    # Get the list of files in both directories
    images_A = os.listdir(dir_A)
    images_B = os.listdir(dir_B)
    
    # Convert list of images in B to a set for faster lookup
    images_B_set = set(images_B)
    
    for image_name in images_A:
        #print(image_name)
        # Check if the image exists in directory B
        assert image_name in images_B_set, f"Error: {image_name} not found in {dir_B}"

    print("All images in Directory A have corresponding images in Directory B.")

# Example usage
dir_A = '/home/vhsillerico/Documents/datasets/carla-night/Town02/rgb_anon'
dir_B = '/home/vhsillerico/Documents/datasets/carla-night/Town02/labelIds'

check_images_in_directories(dir_A, dir_B)