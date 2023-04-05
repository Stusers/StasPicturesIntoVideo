import os
import cv2
import numpy as np
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

image_folder = 'folder_with_images'
output_file = 'my_video.mp4'
fps = 3
size = None  # Set size to None to automatically determine size from the first image

# Get all image files in the folder
image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('.jpg', '.jpeg', '.png'))]

# Load the first image to get the size
img = cv2.imread(image_files[0])
if size is None:
    size = img.shape[1], img.shape[0]

# Create a list of resized and converted images
resized_images = []
for filename in image_files:
    img = cv2.imread(filename)
    if img.shape[1] != size[0] or img.shape[0] != size[1]:
        img = cv2.resize(img, size)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB color channels
    resized_images.append(img)

# Create the video clip from the resized images
try:
    clip = ImageSequenceClip(resized_images, fps=fps)
    clip.write_videofile(output_file)
    print("Video clip created successfully!")
except Exception as e:
    print("Error creating video clip: ", e)