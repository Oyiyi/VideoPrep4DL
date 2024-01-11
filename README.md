# VideoPrep4DL: 3D/Video Data Pre-processing for Deep Learning Networks Training (e.g., CNN/Convolutional Neural Network)

This repository contains code and data for the VideoPrep4DL framework.

## Background and Introduction

Preparing and preprocessing data for deep learning training is one of the most time-consuming (maybe top 1!) and crucial steps in the field of deep learning training. VideoPrep4DL is a comprehensive framework designed to automate the entire data preparation process for a wide range of deep learning applications, including but not limited to CNN (Convolutional Neural Network) training. 

VideoPrep4DL streamlines and automates tasks such as video downloading, video alignment, and more. Our goal is to simplify these often intricate data preparation tasks to save valuable time for researchers and practitioners in the deep learning community, and to minimize debugging efforts during the training phase.

## Features

VideoPrep4DL offers the following features:

- **Video Downloading**: Automatically fetch videos from various sources.
- **Video Alignment**: Align videos to ensure consistent input data for your deep learning models.
- **Data Augmentation**: Apply data augmentation techniques to enhance training data.
- **Easy Configuration**: Customize the preprocessing pipeline to suit your specific requirements.
- **Work in Progress**: Please note that this project is still under active development, and we may continue to update the code and data as we make progress. Be cautious about version control and updates.

## Installation

To get started with VideoPrep4DL, follow these steps:

```bash
# Step 0: clone this repository to your local machine.
git clone https://github.com/your_username/VideoPrep4DL.git
cd VideoPrep4DL
pip install -r requirements.txt

# Step 1: Put the **playlist** link into gen_playlist_urls.py, which will generate the URL links from the playlist into a text file.
python gen_playlist_urls.py

# Step 2: Run main.py to initiate the preprocessing pipeline.
python main.py
