from whisper_timestamped import transcribe as wt
from whisper_timestamped import load_model as wld
import os
import torch

# Global variable to make sure the model loads only the first time
model = None

# Generating Spanish subtitles of the temporal audio with Whisper5

def generate_spanish_subtitles(audio_name):

    global model

    minumum_subtitles_time = 6 # The minimum amount of time a subtitle will span
    maximum_subtitle_time = 10 # The maximum amount of time a subtitle will span
    lines_per_subtitle = 2 # The amount of lines of text in the same subtitle
    # (and go to list_lines directly) if there is too much silence between them

    if not (os.path.exists(f"temp_{audio_name}_audio.wav")):

        print()
        print("Audio not found")
        input()
        
        return None

    # If GPU is available, whisper uses it. Otherwise CPU is used

    if torch.cuda.is_available():
        
        device = "cuda"

    else:

        device = "cpu"

        print("GPU not available, using CPU (slower)")

    # Load small model 

    if model == None:

        model = wld("small").to(device)

    # Subtitle settings and running

    try:

        subtitles = wt(model,

            f"temp_{audio_name}_audio.wav",

            language = "es",
            task = "transcribe",
            fp16 = True if device == "cuda" else False,
            compute_word_confidence = True,
            no_speech_threshold = 0.1,
            compression_ratio_threshold = 1.8,
            condition_on_previous_text = True,
            initial_prompt="THE AUDIO STARTS RIGHT NOW. DO NOT SKIP THE SEGMENT",
            vad = True

        )

        print()
        print(subtitles)

        # Creates subtitles file and saves them as .str (ssf = spanish_subtitles_file)

        with open(f"spanish_subtitles/{audio_name}.srt", "w", encoding = "utf-8") as ssf:

            lines_list = []
            subtitle_start = 0
            subtitle_end = 0
            x = 0
            hours = 0
            minutes = 0
            seconds = 0
            miliseconds = 0

            # For every segment of the subtitles

            for segment in subtitles["segments"]:
                
                # Get the line Spoken into lines_list

                lines_list.append(segment["text"][1:])

                # Save the start time if it is the first line

                if len(lines_list) == 1:

                    subtitle_start = segment["start"]

                # Write in .srt file if is the last line

                elif len(lines_list) >= lines_per_subtitle:

                    subtitle_end = segment["end"]

                    x = x + 1
                    ssf.write(f"{x}\n")

                    hours, minutes, seconds, miliseconds = srt_timelaps_format(subtitle_start)
                    ssf.write(f"{hours}:{minutes}:{seconds},{miliseconds} --> ")

                    hours, minutes, seconds, miliseconds = srt_timelaps_format(subtitle_end) 
                    ssf.write(f"{hours}:{minutes}:{seconds},{miliseconds}\n")

                    # Write the lines

                    print(lines_list)

                    for line in lines_list:

                        # If it is not the last line write just one space between lines

                        if line != lines_list[-1]:

                            ssf.write(f"{line}\n")

                        else:
                            
                            # If it is the last line write two space between lines

                            ssf.write(f"{line}\n\n")

                    lines_list = []

        return audio_name

    except Exception as ae:

        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input()

        return None

    finally:
        
        # Deleting temporal audio

        if os.path.exists(f"temp_{audio_name}_audio.wav"):
           
            os.remove(f"temp_{audio_name}_audio.wav")

def srt_timelaps_format(x):

    seconds = int(x)
                            
    miliseconds = (x - seconds) * 1000
    miliseconds = int(miliseconds)

    hours = seconds/3600

    minutes = (hours - int(hours)) * 60
    hours = int(hours)

    if hours < 10:

        hours = f"0{hours}"

    seconds = (minutes - int(minutes)) *60
    minutes = int(minutes)

    if minutes < 10:

        minutes = f"0{minutes}"

    seconds = int(seconds)

    if seconds < 10:

        seconds = f"0{seconds}"

    return hours, minutes, seconds, miliseconds