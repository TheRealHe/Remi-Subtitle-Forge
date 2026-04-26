from whisper_timestamped import transcribe as wt
from whisper_timestamped import load_model as wld
from modules import support_functions as sf
import pickle as pi
import os

# Global variable to make sure the model loads only the first time

model = None

# Generating Spanish subtitles of the temporal audio with Whisper5

def generate_transcription_subtitles(audio_name):

    global model

    with open("cache/settings.pkl", "rb") as data:

        settings = (pi.load(data))

        # Source language and subtitles settings being defined

        source_lang = settings["input_lan"]
        source_lang = source_lang[0]

        # The maximum amount of time a subtitle will span

        maximum_subtitle_time = settings["maximum_subtitle_time"]

        # The amount of lines of text in the same subtitle
        # (and go to list_lines directly) if there is too much silence between them

        lines_per_subtitle = settings["lines_per_subtitle"] 
        

    if not (os.path.exists(f"temp_{audio_name}_audio.wav")):

        print()
        print("Audio not found")
        input()
        
        return None

    # find device and then does an availability check

    device = sf.device_identifier()

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
            no_speech_threshold = 0.5,
            compression_ratio_threshold = 2,
            condition_on_previous_text = True,
            vad = True

        )

        print()
        print(subtitles)

        # Creates subtitles file and saves them as .str (ssf = spanish_subtitles_file)

        with open(f"transcripted_subtitles/{audio_name}.srt", "w", encoding = "utf-8") as ssf:

            lines_list = []
            subtitle_start = []
            subtitle_end = []
            x = 0
            subtitle_time = 0

            # For every segment of the subtitles

            for segment in subtitles["segments"]:
                
                # Get the line Spoken into lines_list

                lines_list.append(segment["text"][1:])

                # Saves times in lists in case max_check is False to acommodate the lines properly

                subtitle_end.append(segment["end"])
                subtitle_start.append(segment["start"])

                subtitle_time = subtitle_end[-1] - subtitle_start[0]

                # Write in .srt file if is the last line and max time is alr

                if (len(lines_list) >= lines_per_subtitle) and ((subtitle_time) < maximum_subtitle_time):
                    
                    lines_list, subtitle_start, subtitle_end, x = writting_on_srt_True(ssf, subtitle_start[0], subtitle_end[-1], lines_list, x) 

                # Write in .srt file if is the last line and max time is not alr

                elif (len(lines_list) >= lines_per_subtitle) and ((subtitle_time) > maximum_subtitle_time):

                    lines_list, subtitle_start, subtitle_end, x = writting_on_srt_False(ssf, subtitle_start, subtitle_end, lines_list, x, lines_per_subtitle, maximum_subtitle_time)

        return audio_name

    except Exception as ae:

        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        input()

        #return None

    finally:
        
        # Deleting temporal audio

        if os.path.exists(f"temp_{audio_name}_audio.wav"):
           
            os.remove(f"temp_{audio_name}_audio.wav")

# Acommodates time into .srt format

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

# writes on .srt file (original language) when max time is not alr

def writting_on_srt_False(ssf, subtitle_start, subtitle_end, lines_list, x, lines_per_subtitle, maximum_subtitle_time):

    new_lines_list = []
    subtitle_time = 11
    n = lines_per_subtitle - 1


    while subtitle_time > maximum_subtitle_time:

        subtitle_time = subtitle_end[n] - subtitle_start[0]

        if n == 1 and subtitle_time > maximum_subtitle_time:

            subtitle_time = 0
        
        n = n - 1

    # writes subtitle number

    x = x + 1
    ssf.write(f"{x}\n")

    # writes time in correct .srt format

    hours, minutes, seconds, miliseconds = srt_timelaps_format(subtitle_start[0])
    ssf.write(f"{hours}:{minutes}:{seconds},{miliseconds} --> ")

    hours, minutes, seconds, miliseconds = srt_timelaps_format(subtitle_end[n]) 
    ssf.write(f"{hours}:{minutes}:{seconds},{miliseconds}\n")

    print(lines_list)

    # Write the lines

    for i, line in enumerate(lines_list):

        # If lines are inside the max time

        if n > i:

            ssf.write(f"{line}\n")

        # If lines are outside max time

        elif n < i:

            new_lines_list.append(line)

        else:
                                
        # If it is the last line inside the max time

            ssf.write(f"{line}\n\n")

        
    subtitle_end = [subtitle_end[-1]]
    subtitle_start = [subtitle_start[n + 1]]


    return new_lines_list, subtitle_start, subtitle_end, x

# writes on .srt file (original language) when max time is alr

def writting_on_srt_True(ssf, subtitle_start, subtitle_end, lines_list, x):

    # writes subtitle number

    x = x + 1
    ssf.write(f"{x}\n")

    # writes time in correct .srt format

    hours, minutes, seconds, miliseconds = srt_timelaps_format(subtitle_start)
    ssf.write(f"{hours}:{minutes}:{seconds},{miliseconds} --> ")

    hours, minutes, seconds, miliseconds = srt_timelaps_format(subtitle_end) 
    ssf.write(f"{hours}:{minutes}:{seconds},{miliseconds}\n")

    print(lines_list)

    # Write the lines

    for line in lines_list:

        # If it is not the last line write just one space between lines

        if line != lines_list[-1]:

            ssf.write(f"{line}\n")

        else:
                                
        # If it is the last line write two space between lines

            ssf.write(f"{line}\n\n")

    lines_list = []
    subtitle_end = []
    subtitle_start = []

    return lines_list, subtitle_start, subtitle_end, x
