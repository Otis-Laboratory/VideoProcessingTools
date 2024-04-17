import cv2
import concurrent.futures
import imagehash
import os
import time
from PIL import Image

from tools.utils.print_color import MessageType, print_color


def calculate_hash(image):
    # Compute hash using the average hash method
    return imagehash.average_hash(
        Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    )


def deduplicate_frames(input_path, threshold, verbose):
    frame_hashes = {}
    frames_removed = 0
    start_time = time.time()

    print_color(
        f"[INFO] DEDUPLICATING FRAMES FROM {input_path}", MessageType.INFO.value
    )

    with concurrent.futures.ThreadPoolExecutor() as executor:
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

    end_time = time.time()
    time_taken = end_time - start_time
    print_color(
        f"[SUCC] Successfully deduplicated {frames_removed} in {time_taken:.2f} seconds.",
        MessageType.SUCCESS.value,
    )
