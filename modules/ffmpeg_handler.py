import os
from subprocess import run as sr
import pickle as pi

# Extract audio of video - Input is name of the video in folder /video

def extract_audio(video_name):

    # Checking file existence

    if not (os.path.exists(f"input_videos/{video_name}.mp4")):

        print()
        print("❌ Video not found (press enter to continue)")
        input()
        
        return None

    try:

    # Runs "ffmpeg -i "video.mp4" -vn -ar 16000 -ac 1 "audio.wav" in CMD 

        sr([

            "ffmpeg",
            "-i", f"input_videos/{video_name}.mp4",
            "-vn", 
            "-ar", "16000", 
            "-ac", "1",
            "-af", "volume=1.2", 
            f"temp_{video_name}_audio.wav"

 # Captures output and allows Python to check if line fails

], check = True) 
        
        print()
        print(f"Audio successfully extracted: temp_{video_name}_audio.wav") # Confirmation
        print()
        
        return video_name

    # If there is a error finalizes the function.

    except Exception as ae:
            
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input()

        return None
    
# Burns the specified subtitles into the input video

def burn_subtitles(subtitles):

    print()
    print(f"Burning subtittles ({subtitles}) into the video")

    # Gets the task from cache (whatever it is burning the transcriptions or translations)

    with open("cache/settings.pkl", "rb") as data:

        settings = pi.load(data)

        task = settings["task"]
        task = (task.split("_"))[0]

    try:
   
        sr([

            "ffmpeg",
            "-i", f"input_videos/{subtitles}.mp4",
            "-vf", f"subtitles={task}_subtitles/{subtitles}.srt",
            f"output_videos/{subtitles}.mp4"
            
        ], check = True)

        print()
        print("Burning sucessful")

        return subtitles
    
    except FileNotFoundError:

        print("File was not found")
        input()

    except Exception as ae:
            
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input()

        return None
    
# Deletes the process files from the algorithm workflow

def post_process_delete(name):

    try:
    
       os.remove(f"input_videos/{name}.mp4")
       os.remove(f"translated_subtitles/{name}.srt")
       os.remove(f"transcripted_subtitles/{name}.srt")

       print()
       print("Delete succesfully")

    except FileNotFoundError:

        print("File was not found")
        input()

    except Exception as ae:
            
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input()

        return None
    
# Cuts a section of a video

def cut_video(video, start_cut, end_cut):

    print()
    print(f"Cutting video ({video}) as specified")

    try:

        # ffmpeg -i input.mp4 -ss 00:01:00 -t 30 -c:v libx264 -c:a aac output.mp4

        sr(

            ["ffmpeg",
            "-i", f"input_vidoes/{video}",
            "-ss", start_cut,
            "-to", end_cut,
            "-c", "copy", f"input_vidoes/{video}-cut"],

            check = True

        )

        print()
        print("Video cut successfully")
    
    except FileNotFoundError:

        print("File was not found")
        input()

    except Exception as ae:
            
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input()
