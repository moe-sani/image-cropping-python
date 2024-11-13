# image-cropping-python - Image Cropper - Batch Crop and Save Images

This Python project allows you to batch crop multiple images in a folder to a specified size and save the cropped versions to a new folder. The script is designed to be used in a Jupyter Notebook and provides a visual preview of the first few cropped images. This is useful for image preprocessing tasks like dataset preparation, image resizing for thumbnails, and other image manipulation tasks.

## Features
- Batch processing of images from a folder.
- Crops images to a user-defined size.
- Saves the cropped images in a specified output folder.
- Displays a preview of the first few cropped images for quick verification.
  
## Requirements

Before running the notebook, make sure you have the following libraries installed:

- `Pillow` (for image manipulation)
- `matplotlib` (for displaying the cropped image samples)

You can install the necessary libraries using pip:

```bash
pip install pillow matplotlib
```

## Usage

### 1. Clone or download the repository
```bash
git clone git@github.com:moe-sani/image-cropping-python.git
cd image-cropper
```

### 2. Open the Jupyter Notebook
Open the provided Jupyter Notebook (`Image_Cropper.ipynb`) in your local environment.

### 3. Set Parameters
In the notebook, you'll need to set the following parameters:
- **`input_folder`**: Path to the folder containing the images you want to crop.
- **`output_folder`**: Path to the folder where cropped images will be saved.
- **`crop_size`**: Tuple specifying the size of the crop in `(width, height)` format.

For example:
```python
input_folder = 'path/to/your/input/folder'
output_folder = 'path/to/your/output/folder'
crop_size = (300, 300)
```

### 4. Run the Notebook
Execute the notebook cells. The script will:
1. Load images from the input folder.
2. Crop them to the specified size (centered).
3. Save the cropped images to the output folder.
4. Display the first few cropped images as a sample.

### Example Code
Here's a quick look at the core function:

```python
def crop_images(input_folder, output_folder, crop_size, show_samples=3):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get list of image files in input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    
    sample_images = []
    
    for idx, image_file in enumerate(image_files):
        img_path = os.path.join(input_folder, image_file)
        img = Image.open(img_path)

        width, height = img.size
        left = (width - crop_size[0]) / 2
        top = (height - crop_size[1]) / 2
        right = (width + crop_size[0]) / 2
        bottom = (height + crop_size[1]) / 2

        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(os.path.join(output_folder, image_file))

        if idx < show_samples:
            sample_images.append(cropped_img)
    
    return sample_images
```

### 5. Viewing Output
The output folder will contain all the cropped images. In addition, the notebook will display the first few cropped images in a matplotlib plot, which looks like this:

```python
fig, axes = plt.subplots(1, len(cropped_samples), figsize=(15, 5))
for i, img in enumerate(cropped_samples):
    axes[i].imshow(img)
    axes[i].axis('off')
plt.show()
```

### Example Image
Here is an example of how the cropped images will be displayed:

![Sample Image](outputs/road421.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the repository name or any specific paths and details as necessary. You can also include an example image under the "Example Image" section if you'd like to showcase one of the cropped images visually.

Let me know if you need further modifications!