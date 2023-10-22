# Import modules
from tkinter import *
from tkinter.ttk import Treeview
import urllib.request
import io
from PIL import Image, ImageTk
from pytube import YouTube

# Create a root window
root = Tk()

# Get the URL of the video thumbnail
yt = YouTube("https://www.youtube.com/watch?v=sVPYIRF9RCQ")
thumbnail_url = yt.thumbnail_url

# Download the image from the URL and save it in memory
raw_data = urllib.request.urlopen(thumbnail_url).read()
image_data = io.BytesIO(raw_data)

# Open the image from memory and resize it
image = Image.open(image_data)
image = image.resize((100, 100))

# Convert the image to a PhotoImage object
photo = ImageTk.PhotoImage(image)

# Create a Treeview widget
tree = Treeview(root)
tree.pack()

# Insert the image as an item
tree.insert("", "end", text="Video Thumbnail", image=photo)

# Start the main loop
root.mainloop()
