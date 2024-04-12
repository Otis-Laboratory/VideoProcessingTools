import cv2
import imagehash
import os
from PIL import Image


def calculate_hash(image):
    # Make image grayscale for consistency
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Not using this rn, not many improvements, we will see
    # Compute hash using the average hash method
    return imagehash.average_hash(
        Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    )


def deduplicate_frames(input_path, threshold, verbose):
    print("\nNOTE: This script is NOT hung. If you have a slow CPU or a large amount of files, it will take a few minutes to split your data. Please be patient...")
    
    frame_hashes = {}
    frames_removed = 0
    for frame in sorted(os.listdir(input_path)):
        frame_path = os.path.join(input_path, frame)
        image = cv2.imread(frame_path)

        # Calculate hash of the image
        image_hash = calculate_hash(image)

        # Check for similar frames
        duplicate_found = False
        for existing_hash, existing_frame in frame_hashes.items():
            # Compare hashes
            similarity = image_hash - existing_hash
            if similarity < threshold:
                os.remove(frame_path)
                duplicate_found = True
                frames_removed += 1
                if verbose:
                  print(f"Removed duplicate frame {frame_path}")
                break

        if not duplicate_found:
            frame_hashes[image_hash] = frame_path

    print(f"\nSuccessfully deduplicated {frames_removed} frames.")
