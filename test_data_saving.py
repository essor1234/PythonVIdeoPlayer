# Import the csv and os modules
import csv
import os

# Define the directory containing the videos
video_dir = "C:/Users/Videos"

# Define the list of video attributes to store
video_attributes = ["name", "size", "duration", "format"]

# Define the name of the CSV file to store the video info
csv_file = "video_info.csv"

# Open the CSV file in write mode and create a csv.writer object
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    # Write the header row of the CSV file
    writer.writerow(video_attributes)
    # Loop through the video directory and get the video info
    for filename in os.listdir(video_dir):
        # Get the full path of the video file
        filepath = os.path.join(video_dir, filename)
        # Get the size of the video file in bytes
        size = os.path.getsize(filepath)
        # Get the duration of the video file in seconds (you may need to use other libraries for this)
        duration = 0 # Replace this with your code to get the duration
        # Get the format of the video file (you may need to use other libraries for this)
        format = "" # Replace this with your code to get the format
        # Write the video info as a row of the CSV file
        writer.writerow([filename, size, duration, format])
    # Close the CSV file
    f.close()
