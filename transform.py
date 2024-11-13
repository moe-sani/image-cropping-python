import os
import sys
import json
import argparse
from PIL import Image

print(sys.argv[1:])

def crop_image(input_path, output_path, crop_width, crop_height):
    """Crops the image to the specified width and height if valid and saves it to the output path."""
    with Image.open(input_path) as img:
        width, height = img.size
        if width < crop_width or height < crop_height:
            print(f"Skipping {input_path}: Image is smaller than crop dimensions ({crop_width}, {crop_height}).")
            img.save(output_path)  # Save original image as-is
            return False  # Indicate that it was not cropped
        
        # Calculate crop box
        left = (width - crop_width) / 2
        top = (height - crop_height) / 2
        right = (width + crop_width) / 2
        bottom = (height + crop_height) / 2

        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)
        print(f"Saved cropped image to {output_path}")
        return True  # Indicate that it was cropped

def crop_images_in_directory(input_dir, output_dir, crop_width, crop_height):
    """Processes all images in the input directory, cropping and saving them to the output directory.
       Also generates info.labels file in the output directory with metadata for each image."""
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"The input directory {input_dir} does not exist.")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Supported image formats
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp')
    images_processed = 0
    file_data = []

    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(image_extensions):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)
            
            # Crop image and determine cropping status
            cropped = crop_image(input_path, output_path, crop_width, crop_height)
            images_processed += 1
            
            # Append metadata for info.labels
            file_data.append({
                "path": file_name,
                "category": "split",
                "label": { "type": "unlabeled" },
                "metadata": {
                    "Cropped": "Yes" if cropped else "No"
                }
            })
    
    # Generate info.labels file
    info_labels = {
        "version": 1,
        "files": file_data
    }
    
    # Save info.labels to output directory
    with open(os.path.join(output_dir, "info.labels"), "w") as f:
        json.dump(info_labels, f, indent=4)
    
    print(f"Processing complete. {images_processed} images processed.")
    print(f"info.labels file saved in {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Crop all images in a directory to a specified width and height.")
    parser.add_argument("--in-directory", required=True, help="Path to the input directory containing images.")
    parser.add_argument("--out-directory", required=True, help="Path to the output directory for cropped images.")
    parser.add_argument("--crop-width", required=True, type=int, help="Desired crop width.")
    parser.add_argument("--crop-height", required=True, type=int, help="Desired crop height.")
    parser.add_argument("--hmac-key", required=False, type=int, help="hmac-key.")

    args = parser.parse_args()
    
    try:
        crop_images_in_directory(args.in_directory, args.out_directory, args.crop_width, args.crop_height)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
