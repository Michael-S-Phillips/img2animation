#!/bin/bash

# Create the Conda environment
conda env create -f environment.yml

# Activate the environment
conda activate img2ani 

# Install the pip package
pip install imageio-ffmpeg

# Display a message
echo "Environment created and necessary packages installed."

