import os
from subprocess import run as sr
import sys

# Extract audio of video - Input is name of the video in folder /video

def extract_audio(video_name):

    # Checking file existence

    if not (os.path.exists(f"videos/{video_name}.mp4")):

        print()
        print("❌ Video not found (press enter to continue)")
        input()
        
        return None

    try:

    # Runs "ffmpeg -i "video.mp4" -vn -ar 16000 -ac 1 "audio.wav" in CMD 

        sr([

            "ffmpeg",
            "-i", f"videos/{video_name}.mp4",
            "-vn", 
            "-ar", "16000", 
            "-ac", "1",
            "-af", "volume=1.2", 
            f"temp_{video_name}_audio.wav"

 # Captures output and allows Python to check if line fails

], check = True, stdout = sys.stdout, stderr = sys.stderr) 
        
        print()
        print(f"Audio successfully extracted: temp_{video_name}_audio.wav (press enter to continue)") # Confirmation
        input()
        
        return video_name

    # If there is a error finalizes the function.

    except Exception as ae:
            
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input()

        return None