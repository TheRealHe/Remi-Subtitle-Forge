# from modules import ffmpeg_handler as fh
# from modules import youtube_downloader as yd
# from modules import whisper as w
# from modules import nllb_translator as nt

fh_check = True
yd_check = True
w_check = True
nt_check = True

broker = True

# Setting up Menu

while broker:

    option = input("""
        Terminal Menu - Subtitle generator
                   
1. Download Video from YouTube.
2. Create spanish transcription (.str file) of the selected video.
3. Translate Spanish transcription (.str file) to English 
0. closing the program. 
""")
    
    if option == "1":

        if yd_check == True:

            from modules import youtube_downloader as yd

            yd_check = False
        
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

        name = input("""
Enter the name of the video file: """)

        name = fh.extract_audio(name)

        # If name = none it means fh.extract_audio had an exception

        if name != None:

            w.generate_spanish_subtitles(name)
            print()
            input("Press enter to continue ")

    elif option == "3":

        if (nt_check == True):

            from modules import nllb_translator as nt

            nt_check = False

        name = input("""
Enter the name of the spanish .srt file to translate: """)
        print()
        
        nt.srt_translation(name)
    
    elif option == "0":

        broker = False

    else:

        print("")
        print("Enter a correct value (0-2)")
        input()