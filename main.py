import argparse
import os

from tools.utils.print_color import MessageType, print_color

def main():
  parser = argparse.ArgumentParser(description="Video to Dataset - Made by OtisAI")
  parser.add_argument("--input", help="The path to the parent folder of your video(s)")
  parser.add_argument("--output", help="The path to your output folder. You can leave this blank if you'd like one to be created.", default="output")
  parser.add_argument("--skip", help="The amount of frames to skip per second when splitting the video into images. This helps with storage and mitigating duplicates. Default: 23", default=23)
  parser.add_argument("--threshold", help="The threshold to use when deduplicating splitted frames. Recommended: 5-15 Default: 10", default=10)
  parser.add_argument("--verbose", action='store_true', help="Enable verbose mode")
  
  args = parser.parse_args()
  
  input_path = args.input
  output_path = os.path.abspath(args.output)  
  skip = int(args.skip)
  threshold = int(args.threshold)
  verbose = args.verbose
  
  # Evaulate and validate the args
  if not input_path:
    print_color("[ERR] No input path provided.", MessageType.ERROR.value)
    return print_color("[INFO] Usage: main.py [-h] [--input INPUT] [--output OUTPUT] [--skip SKIP] [--threshold THRESHOLD] [--verbose]", MessageType.INFO.value)
  elif not os.path.exists(input_path):
    return print_color(f"[ERR] Input path {os.path.abspath(input_path)} doesn't seem to exist. Please check the path and try again.", MessageType.ERROR.value)
  # Check if output path exists, if not create
  if not os.path.exists(output_path):
    print_color(f"[INFO] {output_path} does not exist, creating now...", MessageType.INFO.value)
    os.makedirs(output_path)
    print_color(f"[INFO] {output_path} created.", MessageType.INFO.value)
  elif os.path.exists(output_path):
    print_color(f"[INFO] {output_path} exists, skipping creation...", MessageType.INFO.value)
  # Warn about improper values
  if skip < 1 or skip > 59:
    print_color(f"[WARN] Skip value less than 1 or greater than 59 may lead to unsatisfactory results. Recommended value: 23 (Anime), 29 (Cinema).", MessageType.WARN.value)
  if threshold < 1 or threshold > 100:
    print_color("[WARN] Threshold value less than 1 or greater than 100 can lead to unsatisfactory results. Recommended value: 10.", MessageType.WARN.value)
  
if __name__ == "__main__":
  main()