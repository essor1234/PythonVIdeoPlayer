# Import the os module
import os
# Define the path of the file or directory you want to get
file_path = '../data/video_data.csv'
# Get the directory where your script is located
script_dir = os.path.dirname (__file__)
# Get the relative path from the script directory
relative_path = os.path.relpath (file_path, script_dir)
# Print the relative path
print (relative_path)