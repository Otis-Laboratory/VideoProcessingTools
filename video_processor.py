import argparse
import os
from utils.handle_video import handle_video

def main():
  parser = argparse.ArgumentParser(description="Video to Dataset - made by otisai")
  parser.add_argument("--input", help="The FULL path to the folder with your video file(s)")
  parser.add_argument("--output", help="The FULL path to your output folder, without quotation marks. You can leave this blank if you'd like one to be created.", default="output")
  parser.add_argument("--skip", help="The amount of frames to skip per second when splitting the video into images. This helps with storage and mitigating duplicates. Default: 23", default=23)
  parser.add_argument("--threshold", help="The threshold to use when deduplicating splitted frames. Recommended: 5-15 Default: 10", default=10)
  parser.add_argument("--verbose", action='store_true', help="Enable verbose mode")
  
  args = parser.parse_args()
  output_path = os.path.abspath(args.output) # Since I abstracted the tools I need to make an absolute path now, or it will create the output folder in the tools folder
  
  handle_video(input_path=args.input, output_path=output_path, skip=int(args.skip), threshold=int(args.threshold), verbose=args.verbose)
  
if __name__ == "__main__":
  main()