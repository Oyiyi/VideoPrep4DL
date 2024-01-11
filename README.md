# VideoPrep4DL: 3D/Video Data Pre-processing for Deep Learning Networks Trainings (e.g. CNN (convolutional neural network))

This repository contains code and data for the....

## Background and Introduction

Preparing and pre-processiong data used for deep learning training is one of the most time c onsuming steps in Deep learning trainings. VideoPrep4DL is a full-stakc framework that helps automating the whole process for various kind of deep learning trainings (e.g. CNN),  from downloading vedios, aligning videos, (expand here).... The idea is to save the communities time and significantly reduce the debugging time due to data pre-processing.,

## Usage

\* **This work is still in progress. We may update the code and data as we make progress. Please be cautious about the version control.**

### Generating and pre-processing videos from scratch

```bash
# Step 1: Put the **playlist** link into gen_playlist_urls.py, which will generates the url links under the playlist into txt file.
python gen_playlist_urls.py

# Step 2: run main.py
python main.py
