# Import the csv and cv2 modules
import csv
import cv2

# Define the name of the CSV file that contains the video info
csv_file = "video_info.csv"

# Open the CSV file in read mode and create a csv.reader object
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    # Skip the header row of the CSV file
    next(reader)
    # Create an empty list to store the video info
    video_list = []
    # Loop through each row of the CSV file and append it as a dictionary to the list
    for row in reader:
        video_dict = {"name": row[0], "size": row[1], "duration": row[2], "format": row[3], "path": row[4]}
        video_list.append(video_dict)
    # Close the CSV file
    f.close()

# Ask the user to enter the name of the video they want to play
video_name = input("Enter the name of the video you want to play: ")

# Find the matching video info from the list and get the file path
video_path = None
for video in video_list:
    if video["name"] == video_name:
        video_path = video["path"]
        break

# If no matching video is found, print an error message and exit
if video_path is None:
    print("No such video found.")
    exit()

# Otherwise, use the cv2 module to play the video file in a new window
else:
    # Create a VideoCapture object from the file path
    cap = cv2.VideoCapture(video_path)
    # Check if the VideoCapture object is opened successfully
    if cap.isOpened() == False:
        print("Error opening video file.")
        exit()

    # Create a named window for displaying the video
    cv2.namedWindow("Video Player", cv2.WINDOW_NORMAL)

    # Loop until the end of the video or until the user presses Q or Esc keys
    while cap.isOpened():
        # Read a frame from the VideoCapture object
        ret, frame = cap.read()
        # If ret is True, display the frame in the window
        if ret == True:
            cv2.imshow("Video Player", frame)
            # Wait for 25 ms or until a key is pressed
            key = cv2.waitKey(25)
            # If Q or Esc keys are pressed, break out of the loop and close the window
            if key == ord("Q") or key == ord("q") or key == 27:
                break
        # If ret is False, break out of the loop and close the window
        else:
            break

    # Release the VideoCapture object and destroy all windows
    cap.release()
    cv2.destroyAllWindows()
