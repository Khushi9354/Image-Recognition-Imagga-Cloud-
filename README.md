# image recognition project using the Imagga Cloud API

# Image Recognition using Imagga Cloud API

This project demonstrates how to use the **Imagga Cloud API** for image recognition and tagging. It retrieves tags for a given image URL and prints them to the console.

## Features

- Uses the Imagga API to fetch tags related to a provided image URL.
- Displays the top 6 tags returned by the API.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/imagga-image-recognition.git
   cd imagga-image-recognition

Install the required libraries:
pip install requests

Usage
Update the API key in the code if necessary.
python image_recognition.py
Code Overview
The script makes a GET request to the Imagga API to fetch tags for a given image URL.

API Key
Make sure to replace the authorization header with your valid Imagga API key and secret. You can find your API key and secret in your Imagga account dashboard.

Acknowledgements
Imagga API Documentation
