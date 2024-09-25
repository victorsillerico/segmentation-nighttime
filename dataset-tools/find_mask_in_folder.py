import os
import shutil

rgb_folder = 'RGB'
masks_folder = 'MASKS_ID'
selected_masks_folder = 'SELECTED_MASKS'

os.makedirs(selected_masks_folder, exist_ok=True)


rgb_images = os.listdir(rgb_folder)


for image_name in rgb_images:
    mask_path = os.path.join(masks_folder, image_name)

    if os.path.exists(mask_path):
        destination_path = os.path.join(selected_masks_folder, image_name)

        shutil.copy2(mask_path, destination_path)
        print(f"Copied {image_name} to SELECTED_MASKS")
    else:
        print(f"No corresponding mask found for {image_name}")
