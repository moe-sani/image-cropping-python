import os
import sys
import argparse
from PIL import Image

print(sys.argv[1:])

def crop_image(input_path, output_path, crop_width, crop_height):
    """Crops the image to the specified width and height if valid and saves it to the output path."""
    with Image.open(input_path) as img:
        width, height = img.size
        if width < crop_width or height < crop_height:
            print(f"Skipping {input_path}: Image is smaller than crop dimensions ({crop_width}, {crop_height}).")
            return
        
        # Calculate crop box
        left = (width - crop_width) / 2
        top = (height - crop_height) / 2
        right = (width + crop_width) / 2
        bottom = (height + crop_height) / 2

        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)
        print(f"Saved cropped image to {output_path}")

def crop_images_in_directory(input_dir, output_dir, crop_width, crop_height):
    """Processes all images in the input directory, cropping and saving them to the output directory."""
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"The input directory {input_dir} does not exist.")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Supported image formats
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp')
    images_processed = 0

    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(image_extensions):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)
            crop_image(input_path, output_path, crop_width, crop_height)
            images_processed += 1
    
    print(f"Processing complete. {images_processed} images processed.")

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
