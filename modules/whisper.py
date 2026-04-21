from whisper_timestamped import transcribe as wt
from whisper_timestamped import load_model as wld
import os
import torch

# Global variable to make sure the model loads only the first time
model = None

# Generating Spanish subtitles of the temporal audio with Whisper5

def generate_spanish_subtitles(audio_name):

    global model

    words_per_line = 10 # Amount of words that there will be per line in a subtitle
    minumum_subtitles_time = 6 # The minimum amount of time a subtitle will span
    lines_per_subtitle = 2 # The amount of lines of text in the same subtitle
    maximum_space_of_time_between_words = 2 # times in seconds for a word to skip the next word
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

        print(subtitles)

        # Creates subtitles file and saves them as .str (ssf = spanish_subtitles_file)

        with open(f"spanish_subtitles/{audio_name}.srt", "a", encoding = "utf-8") as ssf:

            words_list = []
            lines_list = []
            start = 0
            end = 0
            x = 0
            hours = 0
            minutes = 0
            seconds = 0
            miliseconds = 0
            too_long = False

            # For every segment of the subtitles

            for segment in subtitles["segments"]:
                
                # For every word of each segment

                for i, info in enumerate(segment["words"]):
                    
                    # saves word in list

                    words_list.append(info["text"])
                    
                    if ((len(segment["words"]) - 1) > i):

                        if ( segment["words"][i + 1]["start"] - info["end"]) > maximum_space_of_time_between_words:

                            too_long = True
                            
                        else:

                            too_long = False
                    
                    # If first word saves start time

                    if len(words_list) == 1:

                        start = info["start"]

                    # If last word saves end time 

                    if (len(words_list) == words_per_line) or (info["text"] == subtitles["segments"][-1]["words"][-1]["text"]) or (too_long):

                        end = info["end"]

                        # Saves start time for the first line

                        if len(lines_list) == 0:
                            
                            lines_list.append(start)
                
                        # Saves line

                        lines_list.append(words_list.copy())
                        words_list = []

                        print(f"{x+1}: {lines_list}")

                        # If time is alr, or in its the last line in the limit (lines_per_subtitle)
                        # It adds all the information in the file in .srt format

                        if ((len(lines_list) - 1) == lines_per_subtitle) or ((end - lines_list[0]) > minumum_subtitles_time) or (too_long) or (info["text"] == subtitles["segments"][-1]["words"][-1]["text"]):

                            x = x + 1
                            ssf.write(f"{x}\n")
                            
                            hours, minutes, seconds, miliseconds = srt_timelaps_format(lines_list[0])
                            ssf.write(f"{hours}:{minutes}:{seconds},{miliseconds} --> ")

                            hours, minutes, seconds, miliseconds = srt_timelaps_format(end) 
                            ssf.write(f"{hours}:{minutes}:{seconds},{miliseconds}\n")

                            del lines_list[0]

                            for line in lines_list:

                                if line == lines_list[-1]:

                                    ssf.write(f"{' '.join(line)}\n\n")

                                else:

                                    ssf.write(f"{' '.join(line)}\n")

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