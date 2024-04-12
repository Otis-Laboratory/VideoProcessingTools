import cv2
import os

def split_video(input_path, output_path, skip, verbose):
  if not os.path.exists(input_path):
    return print(f"{input_path} doesn't seem to exist or is incorrect. Please try again.")
  elif int(skip) > 59 or int(skip) < 1:
    return print("Please make sure that skip is between 1-59.")
  
  # Create it if it doesn't already exist
  if not os.path.exists(output_path):
    print("Making output folder...")
    os.makedirs(output_path)
    
  # Capture the video
  video = cv2.VideoCapture(input_path)
  
  # Catch an error if it didn't open
  if not video.isOpened():
    print("There was an error while opening the video. Please try again and make a GitHub issue if this persists.")
    
  # Variables for stuff
  frame_count = 0
  frame_index = 0
  video_fc = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
  video_fps = video.get(cv2.CAP_PROP_FPS)
  video_duration = video_fc / video_fps
  video_splitted_fps = video_fc / skip
  
  # Print video information
  print(f"\nVideo Name: {os.path.basename(input_path)}")
  print(f"Video Duration: {video_duration:.2f} seconds")
  print(f"Video FPS: {video_fps:.2f}")
  print(f"Total Frames: {video_fc}")
  print(f"Total Extracted Frames With Skip: {video_splitted_fps:.0f}")
  print(f"Extracting {video_splitted_fps:.0f} frames to: {output_path}")
  print("\nNOTE: This script is NOT hung. If you have a slow CPU or a large amount of files, it will take a few minutes to split your data. Please be patient...")
  
  # Split the frames
  while True:
    # When the video is over, break out of the loop
    success, frame = video.read()
    if not success:
      break
    
    # Skip frames
    if frame_index % skip == 0:
      frame_path = os.path.join(output_path, f"{frame_count:05d}.jpg")
      cv2.imwrite(frame_path, frame)
      if verbose == True:
        print(f"Created {frame_count:05d}.jpg")
      frame_count+=1
      
    # Add 1 to frame count
    frame_index+=1
    
  video.release()
  print(f"\nSuccessfully extracted {video_splitted_fps:.0f} frames to {output_path}")