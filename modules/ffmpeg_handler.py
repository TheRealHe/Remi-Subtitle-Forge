import os
from subprocess import run as sr
import pickle as pi

# Extract audio of video - Input is name of the video in folder /video

def extract_audio(video_name):

    # Checking file existence

    if not (os.path.exists(f"input_videos/{video_name}")):

        print()
        print("❌ Video not found (press enter to continue)")
        input()
        
        return None

    try:

    # Runs "ffmpeg -i "video" -vn -ar 16000 -ac 1 "audio.wav" in CMD 

        name = ".".join((video_name.split("."))[:-1])

        sr([

            "ffmpeg",
            "-i", f"input_videos/{video_name}",
            "-vn", 
            "-ar", "16000", 
            "-ac", "1",
            "-af", "volume=1.2", 
            f"temp_{name}_audio.wav"

 # Captures output and allows Python to check if line fails

], check = True) 
        
        print()
        print(f"Audio successfully extracted: temp_{name}_audio.wav") # Confirmation
        print()
        
        return video_name

    # If there is a error finalizes the function.

    except Exception as ae:
            
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input()

        return None
    
# Burns the specified subtitles into the input video

def burn_subtitles(video):

    name = ".".join((video.split("."))[:-1])

    print()
    print(f"Burning subtittles ({name}) into the video")

    # Gets the task from cache (whatever it is burning the transcriptions or translations)

    with open("cache/settings.pkl", "rb") as data:

        settings = pi.load(data)

        task = settings["task"]
        task = (task.split("_"))[0]

    try:
   
        sr([

            "ffmpeg",
            "-i", f"input_videos/{video}",
            "-vf", f"subtitles={task}_subtitles/{name}.srt",
            f"output_videos/{name}.mp4"
            
        ], check = True)

        print()
        print("Burning sucessful")

        return video
    
    except FileNotFoundError:

        print("File was not found")
        input()

    except Exception as ae:
            
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input()

        return None
    
# Deletes the process files from the algorithm workflow

def post_process_delete(video_name):

    try:
    
        name = ".".join((video_name.split("."))[:-1])

        os.remove(f"input_videos/{video_name}")
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

def cut_video(video):

    # checks if file exists

    if not (os.path.exists(f"input_videos/{video}.mp4")):

        input("❌ Video not found (press enter to continue)")
        
        return None

    # Creates original file name

    cut_video_name = f"{video}-cut-0"

    while os.path.exists(f"input_videos/{cut_video_name}.mp4"):

        cut_video_name = cut_video_name[:-1] + (str(int(cut_video_name[-1]) + 1))

        if cut_video_name[-1] == "9":

            cut_video_name = cut_video_name + "0"

    # Gets and verifies start and ent time of the cut

    print("The time is format is: 00:00:00.000")
    print("The order is: Hours, minutes, seconds and miliseconds")
    print("-------------------------------------------------------")
    print("""Examples:
-------------------------------------------------------   
    - HH:MM:SS.mmm (ej: 01:30:45.500)
    - HH:MM:SS     (ej: 01:30:45)
    - MM:SS.mmm    (ej: 30:45.500)
    - MM:SS        (ej: 30:45)
    - SS.mmm       (ej: 45.500)
    - SS           (ej: 45)""")
    print("-------------------------------------------------------")

    valid_chars = set("0123456789:.")

    start_cut = input("Enter the time in which the cut starts: ")

    while  (not all(c in valid_chars for c in start_cut)) or (start_cut == ""):

        if start_cut == "":

            print("Input is empty...")
            print("Try again")
            print()

        else:

            print("Invalid format. Use numbers, colon (:), or dot (.) only.")
            print("Try again")
            print()

        start_cut = input("Enter the time in which the cut starts: ")

    end_cut = input("Enter the time in which the cut finishes: ")

    while  (not all(c in valid_chars for c in end_cut)) or (end_cut == ""):
        
        if end_cut == "":

            print("Input is empty...")
            print("Try again")
            print()

        else:

            print("Invalid format. Use numbers, colon (:), or dot (.) only.")
            print("Try again")
            print()

        end_cut = input("Enter the time in which the cut finishes: ")

    print()
    print(f"Cutting video ({video}) as specified")

    try:

        # ffmpeg -i input.mp4 -ss 00:01:00 -t 30 -c:v libx264 -c:a aac output.mp4

        sr(

            ["ffmpeg",
            "-i", f"input_videos/{video}.mp4",
            "-ss", start_cut,
            "-to", end_cut,
            "-c", "copy", f"input_videos/{cut_video_name}.mp4"],

            check = True

        )

        print()
        print(f"Video {cut_video_name} cut successfully")

    except Exception as ae:
            
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input()

    finally:

        return cut_video_name

# Combines a dynamic amount of videos together

def concatenate_video():

    # Gets all the videos to concatenate

    videos_to_concatenate = []
    video = ""
    
    print("Enter first video to concatenate:")
    video = input()

    while video != "0":

        if not (os.path.exists(f"input_videos/{video}.mp4")):

            input("❌ Video not found (press enter to continue)")
        
            return None

        videos_to_concatenate.append(video)

        print("Enter next video to concatenate: ")
        print("(Enter 0 if all the videos are already entered)")
        video = input()

    # Creates original file output name

    output_name = "concatenated_video_0"

    while os.path.exists(f"input_videos/{output_name}.mp4"):

        output_name = output_name[:-1] + (str(int(output_name[-1]) + 1))

        if output_name[-1] == "9":

            output_name = output_name + "0"

    # Writes video to concatenate in the .txt file required to run ffmpeg command

    with open("temp_file_videos_to_concatenate.txt", "w") as data:

        for v in videos_to_concatenate:

            data.write(f"file \'input_videos/{v}.mp4\'\n")

    # ffmpeg -f concat -safe 0 -i lista.txt -c copy video_concatenado.mp4

    try:

        sr(
            ["ffmpeg",
            "-f", "concat",
            "-safe", "0",
            "-i", "temp_file_videos_to_concatenate.txt",
            "-c", "copy",f"input_videos/{output_name}.mp4"],

            check = True

            )
        
        print(f"Concatenation ({output_name}) successfully...")
        print()

    except Exception as ae:
            
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input()

    finally:  

        print("Removing temporal files...")

        os.remove("temp_file_videos_to_concatenate.txt")
        
        print("Temporal files were removed")

        return output_name
