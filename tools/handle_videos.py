import os
from tools.utils.print_color import MessageType, print_color
from tools.functions.split_video import split_video
from tools.functions.deduplicate_frames import deduplicate_frames


def handle_videos(input_path, output_path, skip, threshold, verbose):
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.endswith((".mkv", ".mp4")):
                video_path = os.path.join(root, file)  # full path
                filename = os.path.splitext(file)[0]  # get filename without extension
                output_folder = os.path.join(
                    output_path, filename
                )  # create output folder path
                os.makedirs(
                    output_folder, exist_ok=True
                )  # create output folder if not exists
                split_video(video_path, output_folder, skip, verbose)
                deduplicate_frames(output_folder, threshold, verbose)
