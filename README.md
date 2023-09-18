# Image Animation App

The Image Animation App is a Python script that allows you to create animations from a sequence of images. You can load multiple image files, preview the animation, and save it in either GIF or MP4 format.

## 1. Installation

**Clone the Repository:**

```bash
git clone https://github.com/your-username/image-animation-app.git
cd image-animation-app
```

**Create and Activate the Conda Environment:**
To ensure you have the required dependencies, you can create a Conda environment based on the provided environment.yaml file:
```bash
conda env create -f environment.yaml
conda activate img2ani
```
This will set up a Conda environment named img2ani with the necessary packages.

Alternatively, you can run the create_environment.sh script:
```bash
chmod +x create_environment.sh
./create_environment.sh
```
This will perform the above conda commands for you and additionally install imageio-ffmpeg

## 2. Usage
To use the Image Animation App, follow these steps:

Run the script img2ani.py with Python:
```bash
python img2ani.py
```
The app's user interface will open.
Click the "Load Images" button to select multiple image files (e.g., JPG, PNG) that you want to include in the animation.
Choose the animation save format (GIF or MP4) from the dropdown menu.
Adjust the animation speed (frames per second) using the slider.
Click the "Preview Animation" button to preview the animation in a separate window. You can control the playback with the "Play," "Stop," and "Restart" buttons.
Once you are satisfied with the preview, click the "Save Animation" button to save the animation in the selected format.
Specify the output file name and location in the file dialog that appears.
The animation will be saved, and the output path will be displayed in the terminal.

## Features

Load and preview multiple image files.
Create animations in GIF or MP4 format.
Adjust the animation speed.
Play, stop, and restart the animation preview.
Save animations to the specified output file.
Dependencies

The Conda environment defined in environment.yaml includes the following dependencies:

python=3.11
pillow: For image processing.
numpy: For numerical operations.
imageio: For creating animations.
tk: For the graphical user interface.
ffmpeg: For MP4 format support.

## Troubleshooting

For some environments it will be necessary to install imageio-ffmpeg to save out mp4 files. Activate the conda environment and then run:
```bash
pip install imageio-ffmpeg
```