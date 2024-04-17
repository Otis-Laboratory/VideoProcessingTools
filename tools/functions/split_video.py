import os
import cv2

from tools.utils.print_color import MessageType, print_color

def split_video(video_path, output_path, skip, verbose):
  video = cv2.VideoCapture(video_path)

  if not video.isOpened():
    return print_color("[ERR] There was an error while opening the video. Please try again and/or open a GitHub issue if this persists.", MessageType.ERROR.value)
  
  # vars
  frame_count = 0;
  frame_index = 0;
  video_fc = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
  video_fps = video.get(cv2.CAP_PROP_FPS)
  video_duration = video_fc / video_fps
  video_splitted_fc = video_fc / skip

  # print info
  print_color(f"\n[INFO] HANDLING VIDEO {os.path.basename(video_path)}", MessageType.INFO.value)
  print_color(f"\tVideo Duration: {video_duration:.2f} seconds", MessageType.INFO.value)
  print_color(f"\tVideo FPS: {video_fps:.2f}", MessageType.INFO.value)
  print_color(f"\tTotal Frames: {video_fc}", MessageType.INFO.value)
  print_color(f"\tTotal Extracted Frames w/ Skip: {video_splitted_fc:.0f}", MessageType.INFO.value)
  print_color(f"\tExtracting {video_splitted_fc:.0f} frames to \"{output_path}\"", MessageType.INFO.value)

  # splitting
  while True:
    success, frame = video.read()
    if not success:
      break

    if frame_index % skip == 0:
      frame_path = os.path.join(output_path, f"{frame_count:05d}.jpg")
      cv2.imwrite(frame_path, frame)
      if verbose:
        print_color(f"[INFO] Created {frame_count:05d}.jpg", MessageType.INFO.value)  
      frame_count+=1
    
    frame_index+=1
  
  video.release()
  print_color(f"[SUCC] Successfully wrote {video_splitted_fc:.0f} frames to \"{output_path}\"", MessageType.SUCCESS.value)