import os
import time
import cv2
import concurrent.futures

from tools.utils.print_color import MessageType, print_color


def split_video(video_path, output_path, skip, verbose):
    def process_frame(frame_info):
        frame_index, frame = frame_info
        frame_path = os.path.join(output_path, f"{frame_index:05d}.jpg")
        cv2.imwrite(frame_path, frame)
        if verbose:
            print_color(f"[INFO] Created {frame_index:05d}.jpg", MessageType.INFO.value)

    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        return print_color(
            "[ERR] There was an error while opening the video. Please try again and/or open a GitHub issue if this persists.",
            MessageType.ERROR.value,
        )

    # vars
    frame_count = 0
    frame_index = 0
    video_fc = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video_fps = video.get(cv2.CAP_PROP_FPS)
    video_duration = video_fc / video_fps
    video_splitted_fc = video_fc / skip
    start_time = time.time()

    # print info
    print_color(
        f"\n[INFO] HANDLING VIDEO {os.path.basename(video_path)}",
        MessageType.INFO.value,
    )
    print_color(
        f"\tVideo Duration: {video_duration:.2f} seconds", MessageType.INFO.value
    )
    print_color(f"\tVideo FPS: {video_fps:.2f}", MessageType.INFO.value)
    print_color(f"\tTotal Frames: {video_fc}", MessageType.INFO.value)
    print_color(
        f"\tTotal Extracted Frames w/ Skip: {video_splitted_fc:.0f}",
        MessageType.INFO.value,
    )
    print_color(
        f'\tExtracting {video_splitted_fc:.0f} frames to "{output_path}"',
        MessageType.INFO.value,
    )

    # speeds up by 50% using concurrent
    with concurrent.futures.ThreadPoolExecutor() as executor:  # or ProcessPoolExecutor for multi-processing
        while True:
            success, frame = video.read()
            if not success:
                break

            if frame_index % skip == 0:
                executor.submit(process_frame, (frame_count, frame))
                frame_count += 1

            frame_index += 1

    video.release()
    end_time = time.time()
    time_taken = end_time - start_time
    print_color(
        f'[SUCC] Successfully wrote {video_splitted_fc:.0f} frames to "{output_path}" in {time_taken:.2f} seconds.',
        MessageType.SUCCESS.value,
    )
