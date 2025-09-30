JPEG to PNG Image Converter

This Python script automates the process of converting images. It takes an input folder, converts all JPEG (.jpg, .jpeg) images to PNG format, and copies any existing PNG images to a new output folder.
Features

    Converts JPEG images to high-quality PNGs.

    Copies original PNG images without re-compression.

    Ignores other file types and subdirectories.

    Automatically creates the output directory if it does not exist.

    Provides a simple and flexible command-line interface.

Prerequisites

To run this script, you need Python and pip installed on your system. All the necessary Python libraries are listed in the requirements.txt file.

You can install all dependencies at once using pip. This is the recommended method, especially within a container.

pip install -r requirements.txt

How to Run the Script

    Save the Script & Requirements: Save image_converter.py and requirements.txt in the same directory.

    Prepare Your Images: Place all the images you want to process into a single folder.

    Open Your Terminal: Open a command prompt (on Windows) or terminal (on macOS/Linux).

    Navigate to the Script's Directory: Use the cd command to move into the directory where you saved the files.

    Install Dependencies: Run the installation command from the "Prerequisites" section above.

    Execute the Script: Run the script from your terminal, telling it where your images are located.

Command Examples

1. Basic Usage (Default Output Folder)

This is the simplest way to run the script. It will process images from a folder named source_images and create a new folder called png_output in the same directory to store the results.

python image_converter.py ./source_images

2. Specifying a Custom Output Folder

If you want to save the processed images to a specific folder (e.g., converted_images), you can use the -o or --output flag.

python image_converter.py ./source_images -o ./converted_images

The script will print its progress in the terminal, letting you know which files are being converted or copied.