import os
from utils.tools.split_video import split_video
from utils.tools.deduplicate_frames import deduplicate_frames

def handle_video(input_path, output_path, skip, threshold, verbose):
    # Iterate through all files in the input folder
    for file_name in os.listdir(input_path):
        # Check if the file is a video file (you may need to adjust this check based on your file extensions)
        if file_name.endswith(".mp4") or file_name.endswith(".avi") or file_name.endswith(".mkv"):
            video_file_path = os.path.join(input_path, file_name)  # Use a different variable name here
            # Create output folder for each video
            video_output_folder = os.path.join(output_path, os.path.splitext(file_name)[0])
            os.makedirs(video_output_folder, exist_ok=True)
            
            print(f"\n-------------------- Processing Video: {file_name} --------------------")
            print("-------------------- Initializing Video Splitting --------------------")
            split_video(input_path=video_file_path, output_path=video_output_folder, skip=skip, verbose=verbose)
            print("\n------------------ Initializing Frame Deduplication ------------------")
            deduplicate_frames(input_path=video_output_folder, threshold=threshold, verbose=verbose)