# ORB Feature Matching App

## Overview
This project is an **Object Recognition and Feature Matching** application using **ORB (Oriented FAST and Rotated BRIEF)**, a fast and efficient keypoint detection and descriptor extraction algorithm. The app loads reference images, extracts their features, and attempts to recognize objects in a test image by comparing features.

## Features
- Uses **ORB (Oriented FAST and Rotated BRIEF)** for feature extraction
- Loads multiple query images from a folder
- Detects and extracts keypoints and descriptors
- Matches features using **Brute-Force Matcher (BFMatcher)**
- Displays the identified object name on the test image

## Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies:
```bash
pip install opencv-python numpy
```

## Usage
### 1. Prepare Image Data
- Place your reference images in a folder named **`imageQuery`**
- Each image should have a descriptive filename (e.g., `PS4_resident_evil_3.jpg`)

### 2. Run the App
Execute the script with:
```bash
python imageClassification.py
```

### 3. Explanation
- The script loads all images from the `imageQuery` folder
- Extracts **keypoints and descriptors** using ORB
- Reads a **test image**, extracts its features, and matches them against stored descriptors
- Displays the **best match** with the class name overlaid

## Code Structure
```plaintext
├── imageQuery/       # Folder containing reference images
├── maybe/            # Folder containing extra images
├── imageTrain/       # Folder containing test images
├── imageClassification.py           # Main script
├── README.md         # Project documentation
plus extra file for learning purposes
```

## Example Output
When an image is recognized, the class name is displayed on the image:
```
['PS4_resident_evil_3', 'Resident_Evil_7_Biohazard']
Feature descriptors extracted: 2
Matched ID: 1
```

## Future Improvements
- Allow real-time detection via **webcam or video feed**
- Implement **GUI for user interaction**

## License
This project is open-source and available under the MIT License.

