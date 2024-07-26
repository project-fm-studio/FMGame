import tkinter as tk
import pygame
import os
import cv2
from PIL import Image, ImageTk

def play_sound(sound_path):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

root = tk.Tk()
root.title("Project FM [EARLY]")
root.configure(bg="black")

# Get the current working directory
current_directory = os.getcwd()

# Construct the path to the sound and MP4 video relative to the current directory
sound_path = os.path.join(current_directory, "src/game/startupassets/startjingle.wav")
video_path = os.path.join(current_directory, "src/game/startupassets/ProjecTFMlogo.mp4")

# Create a VideoCapture object to read the MP4 video
cap = cv2.VideoCapture(video_path)

# Create a label to display the video frame
video_label = tk.Label(root, bg="black")
video_label.pack()

# Play the sound
play_sound(sound_path)

# Update the video frame periodically
def update_frame():
    ret, frame = cap.read()
    if ret:
        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert the frame to a PhotoImage
        frame_image = ImageTk.PhotoImage(Image.fromarray(frame_rgb))
        video_label.configure(image=frame_image)
        video_label.image = frame_image  # Keep a reference to avoid garbage collection
        root.after(30, update_frame)  # Update every 30 milliseconds
    else:
        cap.release()
start_game = mainloop

# Start updating the frame
update_frame()

root.mainloop()

