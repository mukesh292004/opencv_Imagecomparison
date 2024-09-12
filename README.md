# Image Capture and Comparison Script

## Overview

This Python script captures two images from your webcam and compares them to determine if they are similar. The comparison is done using the Structural Similarity Index (SSIM) provided by the `scikit-image` library.

## Prerequisites

Before running the script, ensure that you have the following Python packages installed:

- `opencv-python` - For capturing images from the webcam.
- `scikit-image` - For comparing images using SSIM.

You can install these packages using `pip`:

```bash
pip install opencv-python scikit-image
