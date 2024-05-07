# Instagram-Like Filters with Convolution
## Introduction

This Python project demonstrates the application of various convolution filters to images, similar to Instagram-like effects. Using OpenCV, this script allows users to apply different filters like sharpening, blurring, and edge detection to modify images interactively. The application is designed to be used with a GUI interface where users can adjust the effects in real-time.
Features

    - Multiple Filters: Apply sharpening, Gaussian blur, and box blur filters.
    - Interactive Adjustments: Use trackbars to adjust contrast, brightness, and filter types dynamically.
    - Grayscale Option: Toggle between color and grayscale modes.
    - Image Saving: Save modified images directly from the application.

## Installation
To get started with this project, you'll need to have Python installed on your system, along with the following Python libraries:

    - OpenCV
    - NumPy
    - Tkinter

### You can install the necessary libraries using pip:

  - bash

  - pip install numpy opencv-python-headless

Note: tkinter typically comes pre-installed with Python, but if it is not available, you can install it based on your operating system.
Usage

### To run the application, execute the script using Python:

- bash

- python image_filter_app.py

### Once the application starts:

    - Use the file dialog to select an image.
    - Adjust the filters and settings using the trackbars in the application window.
    - Press 's' to save the currently displayed image.
    - Press 'q' to exit the application.

## How It Works

The core functionality of this application revolves around the use of convolution kernels. Convolution is a mathematical operation used to extract features from images. Here are the kernels used in this application:

    - Identity Kernel: Leaves the image unchanged.
    - Sharpen Kernel: Enhances the edges in the image.
    - Gaussian Kernel: Blurs the image, reducing noise and detail.
    - Box Kernel: Averages the pixels, producing a blurring effect.

Each filter is applied through the cv2.filter2D function from OpenCV, which performs the convolution between the kernel and the image.
Contributing

Contributions to this project are welcome. Please feel free to fork the repository and submit pull requests.
License

This project is open source and available under the MIT License.

### Acknowledgments
    - Zenva Academy for providing the guidance to create an initial version of this code.
    - OpenCV library for providing extensive tools for image processing.
    - The Python community for continuously supporting and enhancing the Python ecosystem.
