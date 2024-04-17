import multiprocessing
import os
from tools.utils.print_color import MessageType, print_color
from tools.functions.split_video import split_video


def process_video(video_path, output_path, skip, verbose):
    split_video(video_path, output_path, skip, verbose)


def handle_videos(input_path, output_path, skip, threshold, verbose):
    processes = []

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

                # Start a new process to handle each video
                process = multiprocessing.Process(
                    target=process_video,
                    args=(video_path, output_folder, skip, verbose),
                )
                processes.append(process)
                process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()
