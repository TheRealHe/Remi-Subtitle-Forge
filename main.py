# from modules import ffmpeg_handler as fh
# from modules import youtube_downloader as yd
# from modules import whisper as w
# from modules import nllb_translator as nt

def options(option, name = 0):

    broker = True

    fh_check = True
    yd_check = True
    w_check = True
    nt_check = True

    if option == "1":

        if yd_check == True:

            from modules import youtube_downloader as yd

            yd_check = False
        if name == 0:
            
            name = input("""
Name the video file (without extention, just the name): """)

        url = input("""
Enter the URL of the video to download: """)

        yd.download_youtube(url, name)

    elif option == "2":

        if (fh_check == True):

            from modules import ffmpeg_handler as fh

            fh_check = False

        if (w_check == True):

            from modules import whisper as w

            w_check = False

        if name == 0:

            name = input("""
Enter the name of the video file (wihout extension): """)

        name = fh.extract_audio(name)

        # If name = none it means fh.extract_audio had an exception

        if name != None:

            w.generate_spanish_subtitles(name)

            print()
            print("Transcription Sucessfully")

    elif option == "3":

        if (nt_check == True):

            from modules import nllb_translator as nt

            nt_check = False

        if name == 0:

            name = input("""
Enter the name of the spanish .srt file to translate: """)
        print()
        
        nt.srt_translation(name)

    # Burns the specified subtitles into the input video

    elif option == "4":

        if name == 0:
        
            name = input("""
Enter the name of the video file (wihout extension): """)
        
        if (fh_check == True):

            from modules import ffmpeg_handler as fh

            fh_check = False

        fh.burn_subtitles(name)
    
    # Deletes the process files from the algorithm workflow

    elif option == "5":

        if name == 0:

            name = input("""
Enter the name of the files to delete (wihout extension): """)
        
        if (fh_check == True):

            from modules import ffmpeg_handler as fh

            fh_check = False
        
        fh.post_process_delete(name)

    elif option == "0":

        broker = False

    else:

        print("")
        print("Enter a correct value (0-6)")
        input()
    
    return name, broker

# ----------------------------------- The main code starts here -----------------------------------

# Setting up Menu

broker = True

while broker:

    option = input("""
        Terminal Menu - Subtitle generator
                   
1. Download Video from YouTube.
2. Create spanish transcription (.str file) of the selected video.
3. Translate Spanish transcription (.str file) to English
4. Burn the translated subtitle into de original video
5. Delete specified subtitles (.srt files) and input video
6. More options...  
0. closing the program. 
""")
    
    # If the input is a range (example: 2,4) it runs all the steps inside the range (inclusive)

    if  option.count(",") == 1:

        name = 0
        ran = option.split(",")

        for x in range(int(ran[0]), (int(ran[1]) + 1)):

            name, broker = options(str(x), name)

    # If the input is a specific number, the code runs that specific step

    elif option.count(",") == 0: 

        name, broker = options(option)
    
    # If the input has more than a comma (example: 2,3,4), explains the user that is not possible

    else:

        print()
        input("You can write just one comma per request. Example: 2,4")