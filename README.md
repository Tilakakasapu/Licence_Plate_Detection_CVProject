# License Plate Detection Project

## Overview
This project utilizes OpenCV to perform license plate detection in real-time using a webcam. Detected license plates are displayed with bounding boxes and can be saved to a folder named "plates" by pressing the 'S' key.

## Requirements
- Python 3
- OpenCV

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/license-plate-detection.git
   cd license-plate-detection

## Install the required dependencies:

    pip install opencv-python
    Download the Haar Cascade model for license plate detection and place it in the model directory. You can find it here.

## Usage
1. Run the script:
- python license_plate_detection.py
- Use a webcam to capture the video stream.

Detected license plates will be displayed with bounding boxes. Press the 'S' key to save the license plate to the "plates" folder.

## Folder Structure
- model/: Contains the Haar Cascade model for license plate detection.
- plates/: The folder where detected license plates are saved.
## Acknowledgments
- Haar Cascade model for license plate detection: OpenCV GitHub Repository 