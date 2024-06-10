import cv2
import os

def convert_h264_to_png(video_path, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return

    frame_index = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Save the frame as PNG file
        frame_filename = os.path.join(output_folder, f"frame_{frame_index:05d}.png")
        cv2.imwrite(frame_filename, frame)

        frame_index += 1

    cap.release()
    print(f"Conversion complete! Frames saved in {output_folder}")

# Example usage
video_path = "output.h264"
output_folder = "ext_img"
convert_h264_to_png(video_path, output_folder)
