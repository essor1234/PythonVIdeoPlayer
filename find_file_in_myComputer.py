from tkinter import filedialog as fd
import os
# Show a file dialog that only accepts video files
filename = fd.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
# Move the selected video file to a new folder
os.rename(filename, "new_folder/" + os.path.basename(filename))