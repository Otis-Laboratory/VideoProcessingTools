These are my miscellaneous video processing tools that I use to fine-tune SD models and curate pre-train data. Right now, this is just a refurbishment of my existing video splitter and frame deduper, however I plant to add a better version of a booru scraper in the future.

## Features

- Splitting videos into frames
- Customized thresholds and frame-skipping so that you can split how you like

## Setup
```sh
python -m venv venv

# windows
venv/scripts/activate

# unix 
source venv/bin/activate

pip install -r requirements.txt

python video_processor.py --input "path_to_your_videos_folder" --output output --skip 23 --verbose
```

This will iterate through each of the videos in your input folder and create a folder for them in the output location of your choosing. It will split each video into frames by your settings, and then remove duplicate frames.

Note: This script will not automatically delete credits and intros and whatnot from your video, so you will still have to manually delete some parts of your data.

## Requirements
- Operating System: Windows or UNIX-based (tested on Windows 10)
- Python (at least 3.8, tested on 3.10)

## Usage
For ease of use, I've included some command line flags so that you can run this multiple times without having to edit code directly:
- ``--input`` Required: The FULL PATH to the FOLDER with your images. Providing the link to a video itself will lead to an error, so make sure it is a folder.
- ``--output`` Optional: The FULL PATH to the FOLDER where you'd like the frames to be outputted to. By default, an output folder is created in the root directory.
- ``--skip`` Optional: The amount of frames to skip per second when splitting. For example, in a 24FPS video, 23 frames will be skipped and 1 will be kept per second. Avoids waste of storage and duplicates.
- ``--threshold`` Optional: The threshold (sensitivity) of deleting duplicates when deduplicating. **The higher the threshold, the stricter it is (and more duplicates will be removed). The recommended value for this is 10.

## Contributing
Anyone is welcome to contribute to this as long as it provides something meaningful. Do not PR with syntax fixes or comment grammar fixes unless they are breaking.

This project will be rewritten in C/C++.