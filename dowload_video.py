from pytube import YouTube

url = input("Enter the YouTube URL\n")
name = input("Enter the name for the video\n")
name = name + ".mp4"

try:
    print("Downloading starts...\n")
    # Create a YouTube object with the URL
    yt = YouTube(url)
    # Get the highest resolution stream available
    stream = yt.streams.get_highest_resolution()
    # Download the stream and save it as name
    stream.download(filename=name)
    # define path for dowloading
    stream.download(output_path="C:/Users/Downloads")

    print("Download completed..!!")
except Exception as e:
    print(e)
