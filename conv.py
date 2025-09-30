import os
import argparse
from PIL import Image
import shutil

def process_images(input_folder, output_folder):
    """
    Converts JPEG images in a folder to PNG format and copies existing PNGs.

    Args:
        input_folder (str): The path to the folder containing the source images.
        output_folder (str): The path to the folder where the processed images will be saved.
    """
    # Create the output directory if it doesn't already exist.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    # Loop through all files in the input directory.
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Skip if the current item is a directory.
        if os.path.isdir(input_path):
            continue

        # Get the file name without the extension and the extension itself.
        file_base, file_ext = os.path.splitext(filename)
        
        # Standardize the extension to lowercase for comparison.
        file_ext_lower = file_ext.lower()

        # Process JPEG files for conversion.
        if file_ext_lower in ['.jpeg', '.jpg']:
            try:
                with Image.open(input_path) as img:
                    # Define the new filename with a .png extension.
                    output_filename = f"{file_base}.png"
                    output_path = os.path.join(output_folder, output_filename)
                    
                    # Save the image in PNG format.
                    img.save(output_path, 'PNG')
                    print(f"Converted '{filename}' to '{output_filename}'")
            except Exception as e:
                print(f"Error converting '{filename}': {e}")
        
        # Copy existing PNG files.
        elif file_ext_lower == '.png':
            try:
                output_path = os.path.join(output_folder, filename)
                # copy2 preserves file metadata.
                shutil.copy2(input_path, output_path)
                print(f"Copied '{filename}'")
            except Exception as e:
                print(f"Error copying '{filename}': {e}")
        else:
            # Inform the user about skipped files.
            print(f"Skipping non-JPEG/PNG file: '{filename}'")

def main():
    """
    Main function to parse command-line arguments and run the image processing.
    """
    parser = argparse.ArgumentParser(
        description="Convert JPEG images to PNG and copy existing PNGs to a new folder."
    )
    parser.add_argument(
        "input_folder", 
        help="Path to the input folder containing images."
    )
    parser.add_argument(
        "-o", "--output", 
        dest="output_folder",
        help="Path to the output folder. Defaults to a new folder named 'png_output' inside the input folder's parent directory."
    )

    args = parser.parse_args()

    # Determine the output folder path.
    if args.output_folder:
        output_dir = args.output_folder
    else:
        # Default to a folder named 'png_output' in the same directory as the input folder.
        input_parent_dir = os.path.dirname(os.path.abspath(args.input_folder))
        output_dir = os.path.join(input_parent_dir, "png_output")

    process_images(args.input_folder, output_dir)
    print("\nImage processing complete.")

if __name__ == "__main__":
    main()
