# Background Removal Tool - README

## Project Overview
This project provides a Python script to automatically remove the background from images using the `rembg` library and `Pillow`. The tool is intended to be run on a macOS system using Terminal, with VS Code serving as a text editor for script modifications.

## Prerequisites
- Python 3 (preferably installed using Homebrew)
- Virtual environment (`matts_env`) set up for dependency management
- Libraries: `rembg`, `Pillow`

### Installation Instructions

1. **Install Homebrew (if not already installed)**:
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**:
   ```sh
   brew install python
   ```

3. **Set Up Virtual Environment**:
   - Create the project folder and navigate to it:
     ```sh
     cd /Users/mattbaglietto/
     mkdir bg_removal_tool
     cd bg_removal_tool
     ```
   - Create the virtual environment named `matts_env`:
     ```sh
     python3 -m venv matts_env
     ```
   - Activate the virtual environment:
     ```sh
     source matts_env/bin/activate
     ```

4. **Install Required Packages**:
   ```sh
   pip install rembg pillow
   ```

## How to Use the Script

1. **Place the Image in the Project Folder**:
   - Place the image you want to process in the `/Users/mattbaglietto/bg_removal_tool/` folder.
   - Rename it to `input_image.jpg`, or update the file name in the script accordingly.

2. **Edit the Python Script (if necessary)**:
   - Open the `remove_background.py` file in VS Code.
   - Update the `input_path` in the script if your image name is different:
     ```python
     input_path = 'your_image_name.jpg'  # Update with your file name
     ```

3. **Run the Script**:
   - Open Terminal and navigate to the project folder:
     ```sh
     cd /Users/mattbaglietto/bg_removal_tool
     ```
   - Activate the virtual environment:
     ```sh
     source matts_env/bin/activate
     ```
   - Run the Python script:
     ```sh
     python remove_background.py
     ```
   - The script will generate a new image called `output_image.png` with the background removed.

## Optional: Suppress Warnings
If you encounter OpenMP warnings, you can suppress them by setting the environment variable before running the script:
```sh
export KMP_WARNINGS=0
```

## Notes
- Ensure that the virtual environment is always activated before installing packages or running the script.
- The output image will be saved in the same folder as `output_image.png`. The PNG format is used to maintain transparency.

## Future Enhancements
- Add support for specifying the input file name as an argument to make the script more flexible.
- Implement error handling to manage missing files or incorrect paths.
