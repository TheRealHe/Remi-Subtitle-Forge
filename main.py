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
Enter the name of transcripted .srt file to translate: """)
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

            Change_input_language()

        elif option == "2":

            Change_output_language()

        elif option == "0":

            broker = False

        else:

            print("Enter a correct value (0-2)")
            input()

# Change input language

def Change_input_language():

    global input_lan

    available_lan = ["english", "chinese", "german", "spanish", "russian", "korean", "french", "japanese", "portuguese", "turkish", "polish", "catalan", "dutch", "arabic", "swedish", "italian", "indonesian", "hindi", "finnish", "vietnamese", "hebrew", "ukrainian", "greek", "malay", "czech", "romanian", "danish", "hungarian", "tamil", "norwegian", "thai", "urdu", "croatian", "bulgarian", "lithuanian", "latin", "maori", "malayalam", "welsh", "slovak", "telugu", "persian", "latvian", "bengali", "serbian", "azerbaijani", "slovenian", "kannada", "estonian", "macedonian", "breton", "basque", "icelandic", "armenian", "nepali", "mongolian", "bosnian", "kazakh", "albanian", "swahili", "galician", "marathi", "punjabi", "sinhala", "khmer", "shona", "yoruba", "somali", "afrikaans", "occitan", "georgian", "belarusian", "tajik", "sindhi", "gujarati", "amharic", "yiddish", "lao", "uzbek", "faroese", "haitian creole", "pashto", "turkmen", "nynorsk", "maltese", "sanskrit", "luxembourgish", "myanmar", "tibetan", "tagalog", "malagasy", "assamese", "tatar", "hawaiian", "lingala", "hausa", "bashkir", "javanese", "sundanese"]

    lan_codes = {

        "english": ["en", "eng_Latn"],
        "chinese": ["zh", "zho_Hans"], # Chinese code may be problematic as whisper mixes both traditional and simplified
        "german": ["de", "deu_Latn"],
        "spanish": ["es", "spa_Latn"],
        "russian": ["ru", "rus_Cyrl"],
        "korean": ["ko", "kor_Hang"],
        "french": ["fr", "fra_Latn"],
        "japanese": ["ja", "jpn_Jpan"],
        "portuguese": ["pt", "por_Latn"],
        "turkish": ["tr", "tur_Latn"],
        "polish": ["pl", "pol_Latn"],
        "catalan": ["ca", "cat_Latn"],
        "dutch": ["nl", "nld_Latn"],
        "arabic": ["ar", "arb_Arab"],
        "swedish": ["sv", "swe_Latn"],
        "italian": ["it", "ita_Latn"],
        "indonesian": ["id", "ind_Latn"],
        "hindi": ["hi", "hin_Deva"],
        "finnish": ["fi", "fin_Latn"],
        "vietnamese": ["vi", "vie_Latn"],
        "hebrew": ["he", "heb_Hebr"],
        "ukrainian": ["uk", "ukr_Cyrl"],
        "greek": ["el", "ell_Grek"],
        "malay": ["ms", "msa_Latn"],
        "czech": ["cs", "ces_Latn"],
        "romanian": ["ro", "ron_Latn"],
        "danish": ["da", "dan_Latn"],
        "hungarian": ["hu", "hun_Latn"],
        "tamil": ["ta", "tam_Taml"],
        "norwegian": ["no", "nor_Latn"],
        "thai": ["th", "tha_Thai"],
        "urdu": ["ur", "urd_Arab"],
        "croatian": ["hr", "hrv_Latn"],
        "bulgarian": ["bg", "bul_Cyrl"],
        "lithuanian": ["lt", "lit_Latn"],
        "latin": ["la", "lat_Latn"],
        "maori": ["mi", "mri_Latn"],
        "malayalam": ["ml", "mal_Mlym"],
        "welsh": ["cy", "cym_Latn"],
        "slovak": ["sk", "slk_Latn"],
        "telugu": ["te", "tel_Telu"],
        "persian": ["fa", "pes_Arab"],
        "latvian": ["lv", "lav_Latn"],
        "bengali": ["bn", "ben_Beng"],
        "serbian": ["sr", "srp_Cyrl"],
        "azerbaijani": ["az", "aze_Latn"],
        "slovenian": ["sl", "slv_Latn"],
        "kannada": ["kn", "kan_Knda"],
        "estonian": ["et", "est_Latn"],
        "macedonian": ["mk", "mkd_Cyrl"],
        "breton": ["br", "bre_Latn"],
        "basque": ["eu", "eus_Latn"],
        "icelandic": ["is", "isl_Latn"],
        "armenian": ["hy", "hye_Armn"],
        "nepali": ["ne", "nep_Deva"],
        "mongolian": ["mn", "khk_Cyrl"],
        "bosnian": ["bs", "bos_Latn"],
        "kazakh": ["kk", "kaz_Cyrl"],
        "albanian": ["sq", "sqi_Latn"],
        "swahili": ["sw", "swa_Latn"],
        "galician": ["gl", "glg_Latn"],
        "marathi": ["mr", "mar_Deva"],
        "punjabi": ["pa", "pan_Guru"],
        "sinhala": ["si", "sin_Sinh"],
        "khmer": ["km", "khm_Khmr"],
        "shona": ["sn", "sna_Latn"],
        "yoruba": ["yo", "yor_Latn"],
        "somali": ["so", "som_Latn"],
        "afrikaans": ["af", "afr_Latn"],
        "occitan": ["oc", "oci_Latn"],
        "georgian": ["ka", "kat_Geor"],
        "belarusian": ["be", "bel_Cyrl"],
        "tajik": ["tg", "tgk_Cyrl"],
        "sindhi": ["sd", "snd_Arab"],
        "gujarati": ["gu", "guj_Gujr"],
        "amharic": ["am", "amh_Ethi"],
        "yiddish": ["yi", "yid_Hebr"],
        "lao": ["lo", "lao_Laoo"],
        "uzbek": ["uz", "uzn_Latn"],
        "faroese": ["fo", "fao_Latn"],
        "haitian creole": ["ht", "hat_Latn"],
        "pashto": ["ps", "pbt_Arab"],
        "turkmen": ["tk", "tuk_Latn"],
        "nynorsk": ["nn", "nno_Latn"],
        "maltese": ["mt", "mlt_Latn"],
        "sanskrit": ["sa", "san_Deva"],
        "luxembourgish": ["lb", "ltz_Latn"],
        "myanmar": ["my", "mya_Mymr"],
        "tibetan": ["bo", "bod_Tibt"],
        "tagalog": ["tl", "tgl_Latn"],
        "malagasy": ["mg", "mlg_Latn"],
        "assamese": ["as", "asm_Beng"],
        "tatar": ["tt", "tat_Cyrl"],
        "hawaiian": ["haw", "haw_Latn"],
        "lingala": ["ln", "lin_Latn"],
        "hausa": ["ha", "hau_Latn"],
        "bashkir": ["ba", "bak_Cyrl"],
        "javanese": ["jw", "jav_Latn"],
        "sundanese": ["su", "sun_Latn"]
    }

    broker = True

    while broker:

        print("Enter the new input language")
        print("(enter 0 to exit)")
        print("(enter \'help\' to see available input languages)")
        print("--------------------------------------------------")

        option = input()
        print()
        option = (option.lower()).strip()

        if option == "0":

            print("Exiting...")

            return None
        
        elif option == "help":
        
            from modules import support_functions as sf

            sf.print_languages_table(available_lan)

            print()

        elif available_lan.count(option) > 0:
            
            input_lan = lan_codes[option]

            with open("cache/settings.pkl", "wb") as data:

                settings["input_lan"] = input_lan

                pi.dump(settings, data)

            broker = False

        else:

            print("Language not found")
            print()

# Change output language

def Change_output_language():

    global output_lan

    available_lan = ["english", "chinese", "german", "spanish", "russian", "korean", "french", "japanese", "portuguese", "turkish", "polish", "catalan", "dutch", "arabic", "swedish", "italian", "indonesian", "hindi", "finnish", "vietnamese", "hebrew", "ukrainian", "greek", "malay", "czech", "romanian", "danish", "hungarian", "tamil", "norwegian", "thai", "urdu", "croatian", "bulgarian", "lithuanian", "latin", "maori", "malayalam", "welsh", "slovak", "telugu", "persian", "latvian", "bengali", "serbian", "azerbaijani", "slovenian", "kannada", "estonian", "macedonian", "breton", "basque", "icelandic", "armenian", "nepali", "mongolian", "bosnian", "kazakh", "albanian", "swahili", "galician", "marathi", "punjabi", "sinhala", "khmer", "shona", "yoruba", "somali", "afrikaans", "occitan", "georgian", "belarusian", "tajik", "sindhi", "gujarati", "amharic", "yiddish", "lao", "uzbek", "faroese", "haitian creole", "pashto", "turkmen", "nynorsk", "maltese", "sanskrit", "luxembourgish", "myanmar", "tibetan", "tagalog", "malagasy", "assamese", "tatar", "hawaiian", "lingala", "hausa", "bashkir", "javanese", "sundanese"]

    lan_codes = {

        "english": "eng_Latn",
        "chinese": "zho_Hans",
        "german": "deu_Latn",
        "spanish": "spa_Latn",
        "russian": "rus_Cyrl",
        "korean": "kor_Hang",
        "french": "fra_Latn",
        "japanese": "jpn_Jpan",
        "portuguese": "por_Latn",
        "turkish": "tur_Latn",
        "polish": "pol_Latn",
        "catalan": "cat_Latn",
        "dutch": "nld_Latn",
        "arabic": "arb_Arab",
        "swedish": "swe_Latn",
        "italian": "ita_Latn",
        "indonesian": "ind_Latn",
        "hindi": "hin_Deva",
        "finnish": "fin_Latn",
        "vietnamese": "vie_Latn",
        "hebrew": "heb_Hebr",
        "ukrainian": "ukr_Cyrl",
        "greek": "ell_Grek",
        "malay": "msa_Latn",
        "czech": "ces_Latn",
        "romanian": "ron_Latn",
        "danish": "dan_Latn",
        "hungarian": "hun_Latn",
        "tamil": "tam_Taml",
        "norwegian": "nor_Latn",
        "thai": "tha_Thai",
        "urdu": "urd_Arab",
        "croatian": "hrv_Latn",
        "bulgarian": "bul_Cyrl",
        "lithuanian": "lit_Latn",
        "latin": "lat_Latn",
        "maori": "mri_Latn",
        "malayalam": "mal_Mlym",
        "welsh": "cym_Latn",
        "slovak": "slk_Latn",
        "telugu": "tel_Telu",
        "persian": "pes_Arab",
        "latvian": "lav_Latn",
        "bengali": "ben_Beng",
        "serbian": "srp_Cyrl",
        "azerbaijani": "aze_Latn",
        "slovenian": "slv_Latn",
        "kannada": "kan_Knda",
        "estonian": "est_Latn",
        "macedonian": "mkd_Cyrl",
        "breton": "bre_Latn",
        "basque": "eus_Latn",
        "icelandic": "isl_Latn",
        "armenian": "hye_Armn",
        "nepali": "nep_Deva",
        "mongolian": "khk_Cyrl",
        "bosnian": "bos_Latn",
        "kazakh": "kaz_Cyrl",
        "albanian": "sqi_Latn",
        "swahili": "swa_Latn",
        "galician": "glg_Latn",
        "marathi": "mar_Deva",
        "punjabi": "pan_Guru",
        "sinhala": "sin_Sinh",
        "khmer": "khm_Khmr",
        "shona": "sna_Latn",
        "yoruba": "yor_Latn",
        "somali": "som_Latn",
        "afrikaans": "afr_Latn",
        "occitan": "oci_Latn",
        "georgian": "kat_Geor",
        "belarusian": "bel_Cyrl",
        "tajik": "tgk_Cyrl",
        "sindhi": "snd_Arab",
        "gujarati": "guj_Gujr",
        "amharic": "amh_Ethi",
        "yiddish": "yid_Hebr",
        "lao": "lao_Laoo",
        "uzbek": "uzn_Latn",
        "faroese": "fao_Latn",
        "haitian creole": "hat_Latn",
        "pashto": "pbt_Arab",
        "turkmen": "tuk_Latn",
        "nynorsk": "nno_Latn",
        "maltese": "mlt_Latn",
        "sanskrit": "san_Deva",
        "luxembourgish": "ltz_Latn",
        "myanmar": "mya_Mymr",
        "tibetan": "bod_Tibt",
        "tagalog": "tgl_Latn",
        "malagasy": "mlg_Latn",
        "assamese": "asm_Beng",
        "tatar": "tat_Cyrl",
        "hawaiian": "haw_Latn",
        "lingala": "lin_Latn",
        "hausa": "hau_Latn",
        "bashkir": "bak_Cyrl",
        "javanese": "jav_Latn",
        "sundanese": "sun_Latn"
    }

    broker = True

    while broker:

        print("Enter the new output language")
        print("(enter 0 to exit)")
        print("(enter \'help\' to see available input languages)")
        print("--------------------------------------------------")

        option = input()
        print()
        option = (option.lower()).strip()

        if option == "0":

            print("Exiting...")

            return None
        
        elif option == "help":
        
            from modules import support_functions as sf

            sf.print_languages_table(available_lan)

            print()

        elif available_lan.count(option) > 0:
            
            output_lan = lan_codes[option]

            with open("cache/settings.pkl", "wb") as data:

                settings["output_lan"] = output_lan

                pi.dump(settings, data)

            broker = False

        else:

            print("Language not found")
            print()

# ------------------- Manage AI Translation Models Menu -------------------

def manage_AI_translation_models():

    broker = True

    global translation_AI_model_being_used, installed_translation_AI_models
        
    while broker:

        option = input(f"""
-------------------------------------------------------
            AI translation models - Menu
-------------------------------------------------------
current AI translation model being used:
{translation_AI_model_being_used[:-4]}

1. Change current AI translation model being used
2. Install new AI translation model
3. Delete existent AI translation model

0. Go back to more options 
-------------------------------------------------------
                   
""")
    
        print()

        if option == "1":

            print("All installed AI translation models are: ")
            print("----------------------------------------")

            chosen_model = ""
            exists = True

            for i, model in enumerate(installed_translation_AI_models):

                print(f"{i+1}. {model}")

            print("----------------------------------------")

            while (type(chosen_model) != int) or exists:
                
                try:

                    print("Choose one of these models (enter the number)")
                    print("(enter 0 to exit):")

                    chosen_model = int(input())
                    
                    chosen_model = abs(chosen_model)

                except ValueError:

                    print("Input must be a whole number")
                    print("Try again")
                    print() 

                if chosen_model == 0:

                    print("Exiting...")
                    print()

                    break

                elif (type(chosen_model) == int):

                    try:
                        
                        translation_AI_model_being_used = installed_translation_AI_models[chosen_model-1]
                        exists = False

                    except IndexError:

                        print("Input must be one of the numbers in the previously showed models list")
                        print("Try again")
                        print()

                        chosen_model = ""

            settings["translation_AI_model_being_used"] = translation_AI_model_being_used 

            with open("cache/settings.pkl", "wb") as data:

                pi.dump(settings, data) 


            print("Current AI translation model being used has succesfully changed to:")
            print(translation_AI_model_being_used)
            print()

        elif option == "2":


            model_path = choosing_NLLB_model_to_install()

            if model_path != 0:

                print("---------------------------------------------------")
                print("Enter the new model desired quantization")
                print("Example: int8")
                print("Make sure specified quantization is posible in this model")
                print("----------------------------------------------------------")
                qua = input()
                print()

                from modules import installing as ins

                ins.install_translation_model_ct2(model_path, qua)

            else:

                print("Exiting...")
                print()

        elif option == "3":

            print("All installed AI translation models are: ")
            print("----------------------------------------")

            chosen_model = ""
            exists = True

            for i, model in enumerate(installed_translation_AI_models):

                print(f"{i+1}. {model}")

            print("----------------------------------------")

            while (type(chosen_model) != int) or exists:
                
                try:

                    print("Choose one of these models (enter the number):")
                    print("(enter 0 to exit):")

                    chosen_model = int(input())
                    
                    chosen_model = abs(chosen_model)

                except ValueError:

                    print("Input must be a whole number")
                    print("Try again")
                    print() 

                if chosen_model == 0:

                    print("Exiting...")
                    print()

                    break

                elif (type(chosen_model) == int):

                    try:
                        
                        from modules import installing as ins

                        model_to_delete = installed_translation_AI_models[chosen_model-1]

                        ins.delete_translation_model(model_to_delete)

                        exists = False

                    except IndexError:

                        print("Input must be one of the numbers in the previously showed models list")
                        print("Try again")
                        print()

                        chosen_model = ""

        elif option == "0":

            broker = False

        else:

            print("Enter a correct value (0-4)")
            input()

# Menu to select which NLB model to install

def choosing_NLLB_model_to_install():
     
    broker = True

    check_one = "not installed"
    check_two = "not installed"
    check_three = "not installed"
    
    import pickle as pi

    with open("cache/settings.pkl", "rb") as data:

        settings = pi.load(data)

    if (settings["installed_translation_AI_models"]).count("facebook/nllb-200-distilled-600M-ct2") > 0:

        check_one = "installed"

    if (settings["installed_translation_AI_models"]).count("facebook/nllb-200-distilled-1.3B-ct2") > 0:

        check_two = "installed"

    if (settings["installed_translation_AI_models"]).count("facebook/nllb-200-3.3B-ct2") > 0:

        check_three = "installed"

    while broker:

        option = input(f"""
----------------------------------------------------
            Choose NLLB Model to Install
----------------------------------------------------      
1. nllb-200-distilled-600M ({check_one})
2. nllb-200-distilled-1.3B ({check_two})
3. nllb-200-3.3B ({check_three})
  
0. Go back to more options 
---------------------------------------------------- 
                   
""")
    
        print()

        if option == "1":

            if check_one == "installed":

                print("This model is already installed")
                print("Delete and re install if you want to update")
                print()

            else:
                
                return "facebook/nllb-200-distilled-600M"

        elif option == "2":

            if check_two == "installed":

                print("This model is already installed")
                print("Delete and re install if you want to update")
                print()

            else:

                return "facebook/nllb-200-distilled-1.3B"
            
        elif option == "3":

            if check_three == "installed":

                print("This model is already installed")
                print("Delete and re install if you want to update")
                print()

            else:

                return "facebook/nllb-200-3.3B"

        elif option == "0":

            broker = False

        else:

            print("Enter a correct value (0-3)")
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

    from modules import installing as ins

    with open("cache/computer_information.pkl", "rb") as data:

        computer_information = pi.load(data)

    GPUs = ins.gpu_detecter()

    print("These GPUS were found")
    print()
    print(f"Current device being used for AI is {computer_information["GPU"]}") 
    print("----------------------------------")

    for i, gpu in enumerate(GPUs):

        print(f"{i+1}. {gpu}")

    print("----------------------------------")

    chosen_gpu = ""

    while (type(chosen_gpu) != int) or exists:
                
        try:

            print("Choose one of these GPUs (enter the number)")
            print("(enter 0 to exit):")

            chosen_gpu = int(input())
                    
            chosen_gpu = abs(chosen_gpu)

        except ValueError:

            print("Input must be a whole number")
            print("Try again")
            print() 

        if chosen_gpu == 0:

            print("Exiting...")
            print()

            break

        elif (type(chosen_gpu) == int):

            try:
                
                computer_information["GPU"] = ins.gpu_chooser([GPUs[chosen_gpu-1]])

                with open("cache/computer_information.pkl", "wb") as data:

                    pi.dump(computer_information, data)

                print(f"The device used for the AIs has changed to {computer_information["GPU"]}")
                
                exists = False

            except IndexError:

                print("Input must be one of the numbers in the previously showed models list")
                print("Try again")
                print()

                chosen_gpu = ""

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
    installed_translation_AI_models = settings["installed_translation_AI_models"]

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