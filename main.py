# from modules import ffmpeg_handler as fh
# from modules import youtube_downloader as yd
# from modules import whisper as w
# from modules import nllb_translator as nt

# ----------------------------------------- Main Menu ----------------------------------

def options(option, name = 0):

    broker = True

    if option == "1":

        print()
        print("Loading...")

        from modules import youtube_downloader as yd

        if name == 0:
            
            name = input("""
Name the video file (without extention, just the name): """)

        url = input("""
Enter the URL of the video to download: """)

        yd.download_youtube(url, name)

    elif option == "2":

        print()
        print("Loading...")

        from modules import ffmpeg_handler as fh
        from modules import whisper as w

        if name == 0:

            name = input("""
Enter the name of the video file (wihout extension): """)

        name = fh.extract_audio(name)

        # If name = none it means fh.extract_audio had an exception

        if name != None:

            w.generate_transcription_subtitles(name)

            print()
            print("Transcription Sucessfully")

    elif option == "3":

        print()
        print("Loading...")

        from modules import nllb_translator as nt

        if name == 0:

            name = input("""
Enter the name of the spanish .srt file to translate: """)
        print()
        
        nt.srt_translation(name)

    # Burns the specified subtitles into the input video

    elif option == "4":

        print()
        print("Loading...")

        if name == 0:
        
            name = input("""
Enter the name of the video file (wihout extension): """)
        
        from modules import ffmpeg_handler as fh

        fh.burn_subtitles(name)
    
    # Deletes the process files from the algorithm workflow

    elif option == "5":

        print()
        print("Loading...")
            
        if name == 0:

            name = input("""
Enter the name of the files to delete (wihout extension): """)
        
        from modules import ffmpeg_handler as fh
        
        fh.post_process_delete(name)

    elif option == "6":

        more_options_menu()

    elif option == "0":

        broker = False

    else:

        print("Enter a correct value (0-6)")
        input()

        return None, "False"
    
    return name, broker

# ------------------------------------ More Options Menu ------------------------------------ 

def more_options_menu():

    broker = True

    while broker:

        option = input("""
---------------------------------------------------
                More Options - Menu
---------------------------------------------------        
1. Manage languages (input and output)
2. Manage AI translation models
3. Change whisper parameters
4. Change subtitulation task
5. Update computer information in cache
6. Other tools (basic video editing)
  
0. Go back to main menu 
---------------------------------------------------
                   
""")
    
        print()

        if option == "1":

            manage_languages()

        elif option == "2":

            manage_AI_translation_models()

        elif option == "3":

            change_whisper_parameters()

        elif option == "4":

            change_subtitulation_task()

        elif option == "5":

            update_computer_information_in_cache()

        elif option == "6":

            other_tools()

        elif option == "0":

            broker = False
        
        else:

            print("Enter a correct value (0-4)")
            input()

# --------------------------- Manage Languages Menu -------------------------

def manage_languages():

    broker = True

    global input_lan 
    global output_lan 

    while broker:

        option = input(f"""
-------------------------------------------------------
                Manage Languages - Menu
-------------------------------------------------------        
1. Change input language (current: {input_lan[0]}, {input_lan[1]})
2. Change output language (current: {output_lan})
  
0. Go back to more options 
-------------------------------------------------------
                   
""")
    
        print()

        if option == "1":

            print("Building...")

        elif option == "2":

            print("Building...")

        elif option == "0":

            broker = False

        else:

            print("Enter a correct value (0-2)")
            input()

# Change input language

def Change_input_language():

    print("me woa matar")

# ------------------- Manage AI Translation Models Menu -------------------

def manage_AI_translation_models():

    broker = True

    global translation_AI_model_being_used
        
    while broker:

        option = input(f"""
-------------------------------------------------------
            AI translation models - Menu
-------------------------------------------------------
current AI translation model being used:
{translation_AI_model_being_used[:-4]}

1. Change current AI translation model being used
2. Install new AI translation model
3. Update existent AI translation model
4. Delete existent AI translation model

0. Go back to more options 
-------------------------------------------------------
                   
""")
    
        print()

        if option == "1":

            print("Building...")

        elif option == "2":

            print("Building...")

        elif option == "3":

            print("Building...")

        elif option == "4":

            print("Building...")

        elif option == "0":

            broker = False

        else:

            print("Enter a correct value (0-4)")
            input()

# ------------------- Change Whisper Parameters Menu -------------------

def change_whisper_parameters():

    broker = True

    global whisper_model_size, lines_per_subtitle, maximum_subtitle_time 

    while broker:

        option = input(f"""
----------------------------------------------------------
            Change Whisper Parameters - Menu
----------------------------------------------------------
Current whisper parameters being used:
                       
- whisper model size: {whisper_model_size}
- maximum subtitle time: {maximum_subtitle_time}
- lines of text per subtitle: {lines_per_subtitle}

1. Change <whisper model size> parameter
2. Change <maximum subtitle time> parameter
3. Change <lines of text per subtitle> parameter

0. Go back to more options 
----------------------------------------------------------
                   
""")
    
        print()

        if option == "1":

            change_whisper_model_size_parameter()

        elif option == "2":

            print("Changing...")

            x = "a"

            while type(x) != float:
                
                try:

                    x = float(input("New maximum subtitle time = "))
                
                except ValueError:

                    print("New maximum subtitle time parameter must be a positive decimal number")
                    print("Try again")
                    print()

            x = abs(x)

            settings["maximum_subtitle_time"] = x

            with open("cache/settings.pkl", "wb") as data:

                pi.dump(settings, data)

            maximum_subtitle_time  = settings["maximum_subtitle_time"]

            print(f"New maximum subtitle time parameter changed successfully to {maximum_subtitle_time}")
            print()

        elif option == "3":

            print("Changing...")

            x = "a"

            while type(x) != int:
                
                try:

                    x = int(input("New lines of text per subtitle = "))
                
                except ValueError:

                    print("lines of text per subtitle parameter must be a whole number")
                    print("Try again")
                    print()

            x = abs(x)

            settings["lines_per_subtitle"] = x

            with open("cache/settings.pkl", "wb") as data:

                pi.dump(settings, data)

            lines_per_subtitle  = settings["lines_per_subtitle"]

            print(f"lines of text per subtitle parameter changed successfully to {lines_per_subtitle}")
            print()

        elif option == "0":

            broker = False

        else:

            print("Enter a correct value (0-3)")
            input()

# Changes the size parameter of whisper model

def change_whisper_model_size_parameter():

    print("Changing...")

    broker = True

    global whisper_model_size

    while broker:

        option = input(f"""
----------------------------------------------------------
                Whisper Model Size Options
----------------------------------------------------------
Current whisper model size: being used: {whisper_model_size}

1. Change model size to <tiny> (1 GB VRAM REQUIRED)
2. Change model size to <base> (1 GB VRAM REQUIRED)
3. Change model size to <small> (2 GB VRAM REQUIRED)
4. Change model size to <medium> (5 GB VRAM REQUIRED)
5. Change model size to <large> (10 GB VRAM REQUIRED)
6. Change model size to <turbo> (6 GB VRAM REQUIRED)

0. Go back to change whisper parameters
----------------------------------------------------------
                    
""")
        
        print()

        broker = False

        if option == "1":

            settings["whisper_model_size"] = "tiny"

        elif option == "2":

            settings["whisper_model_size"] = "base"

        elif option == "3":

            settings["whisper_model_size"] = "small"
        
        elif option == "4":

            settings["whisper_model_size"] = "medium"

        elif option == "5":

            settings["whisper_model_size"] = "large"

        elif option == "6":

            settings["whisper_model_size"] = "turbo"
            

        elif option == "0":

            break

        else:

            broker = True

            print("Enter a correct value (0-6)")
            input()

    with open("cache/settings.pkl", "wb") as data:

        pi.dump(settings, data)

    whisper_model_size = settings["whisper_model_size"]

    print(f"whisper model size changed successfully to {whisper_model_size}")
    print()

# ------------------- Change Subtitulation Task "Menu" -------------------

def change_subtitulation_task():

    broker = True

    global task
        
    while broker:

        option = input(f"""
----------------------------------------------------------
            Change Subtitulation Task - Menu
----------------------------------------------------------
"Task" is which subtitulation is being burned into
the output video. The transcripted or the translated
Current task is: {task}
                       
1. Change task to <translated_subtitulation>
2. Change task to <transcripted_subtitulation>

0. Go back to more options 
----------------------------------------------------------
                   
""")
    
        print()

        if option == "1":

            print("Changing...")

            settings["task"] = "translated_subtitulation"

            with open("cache/settings.pkl", "wb") as data:

                pi.dump(settings, data)

            task = "translated_subtitulation"

            print(f"Task changed successfully to {task}")
            print()

        elif option == "2":

            print("Changing...")

            settings["task"] = "transcripted_subtitulation"

            with open("cache/settings.pkl", "wb") as data:

                pi.dump(settings, data)

            task = "transcripted_subtitulation"

            print(f"Task changed successfully to {task}")
            print()

        elif option == "0":

            broker = False

        else:

            print("Enter a correct value (0-2)")
            input()

# ---------- Update Computer Information in Cache Fucntion ----------

def update_computer_information_in_cache():

    print("I have no idea yet")
    print()

# ------------------------- Other Tools Menu -------------------------

def other_tools():

    broker = True
        
    while broker:

        option = input(f"""
--------------------------------------------------
                Other Tools - Menu
--------------------------------------------------                    
1. I will put stuff in here eventually...
2. miau

0. Go back to more options 
--------------------------------------------------
                   
""")
    
        print()

        if option == "1":

            print("Building...")

        elif option == "2":

            print("Building...")

        elif option == "0":

            broker = False

        else:

            print("Enter a correct value (0-2)")
            input()

# ----------------------------------- The main code starts here -----------------------------------

# Setting up Menu

import pickle as pi

# Reading settings

with open("cache/settings.pkl", "rb") as data:

    settings = (pi.load(data))

    translation_AI_model_being_used = settings["translation_AI_model_being_used"]
    input_lan = settings["input_lan"]
    output_lan = settings["output_lan"]
    whisper_model_size = settings["whisper_model_size"]
    maximum_subtitle_time = settings["maximum_subtitle_time"]
    lines_per_subtitle = settings["lines_per_subtitle"]
    task = settings["task"]

broker = True

while broker:

    option = input(f"""
--------------------------------------------------------------------------
                    Terminal Menu - Subtitle generator
--------------------------------------------------------------------------                 
1. Download video from YouTube.
2. Create video transcription (.str file) in {input_lan[0]}, {input_lan[1]}
3. Translate transcription (.str file) to {output_lan}
4. Burn {(task.split("_"))[0]} subtitles into de original video
5. Delete specified subtitles (.srt files) and input video
6. More options...
  
0. close the program. 
--------------------------------------------------------------------------
(It is possible to run a range of steps. For example: 2,4 will run steps: 2,3,4)
                   
""")
    
    # If the input is a range (example: 2,4) it runs all the steps inside the range (inclusive)

    if  option.count(",") == 1:

        name = 0
        ran = option.split(",")

        for x in range(int(ran[0]), (int(ran[1]) + 1)):

            name, broker = options(str(x), name)

            if broker == "False":

                break

    # If the input is a specific number, the code runs that specific step

    elif option.count(",") == 0: 

        name, broker = options(option)
    
    # If the input has more than a comma (example: 2,3,4), explains the user that is not possible

    else:

        print()
        input("You can write just one comma per request. Example: 2,4")