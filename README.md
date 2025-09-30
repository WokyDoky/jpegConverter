# JPEG to PNG Image Converter

CLI tool to batch convert JPEG images to PNG format while preserving existing PNGs.

This Python script automates the process of converting images. It takes an input folder, converts all JPEG (`.jpg`, `.jpeg`) images to PNG format, and copies any existing PNG images to a new output folder.

---

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

You need **Python 3.x** and **pip** installed on your system.

### Installation


1.  **Clone the repository** (or download the files into a single directory):
    ```bash
    git clone https://github.com/WokyDoky/jpegConverter
    cd 
    ```

2.  **Install the required Python libraries** from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```


## 🚀 How to Use

Once installed, you can run the script from your terminal.

1. Prepare Your Images: Place all the images you want to process into a single folder.

2. Open Your Terminal: Open a command prompt (on Windows) or terminal (on macOS/Linux).

3. Navigate to the Script's Directory: Use the cd command to move into the directory where you saved the files.

4. Install Dependencies: Run the installation command from the "Prerequisites" section above.

5. Execute the Script: Run the script from your terminal, telling it where your images are located.

### Command Examples

```bash
python image_converter.py ./source_images
```

**Specifying a Custom Output Folder**

If you want to save the processed images to a specific folder (e.g., converted_images), you can use the -o or --output flag.

```bash
python image_converter.py ./source_images -o ./converted_images
```