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

    available_lan = [
    "acehnese (arabic)", "acehnese (latin)", "mesopotamian arabic", "ta'izzi-adeni arabic",
    "tunisian arabic", "afrikaans", "south levantine arabic", "akan", "amharic",
    "north levantine arabic", "modern standard arabic", "najdi arabic", "moroccan arabic",
    "egyptian arabic", "assamese", "asturian", "awadhi", "central aymara", "south azerbaijani",
    "north azerbaijani", "bashkir", "bambara", "balinese", "belarusian", "bemba", "bengali",
    "bhojpuri", "banjar (arabic)", "banjar (latin)", "standard tibetan", "bosnian", "buginese",
    "bulgarian", "catalan", "cebuano", "czech", "chokwe", "central kurdish", "crimean tatar",
    "welsh", "danish", "german", "southwestern dinka", "dyula", "dzongkha", "greek", "english",
    "esperanto", "estonian", "basque", "ewe", "faroese", "fijian", "finnish", "fon", "french",
    "friulian", "nigerian fulfulde", "scottish gaelic", "irish", "galician", "guarani",
    "gujarati", "haitian creole", "hausa", "hebrew", "hindi", "chhattisgarhi", "croatian",
    "hungarian", "armenian", "igbo", "ilocano", "indonesian", "icelandic", "italian", "javanese",
    "japanese", "kabyle", "jingpho", "kamba", "kannada", "kashmiri (arabic)", "kashmiri (devanagari)",
    "georgian", "central kanuri (arabic)", "central kanuri (latin)", "kazakh", "kabiyè",
    "kabuverdianu", "khmer", "kikuyu", "kinyarwanda", "kyrgyz", "kimbundu", "northern kurdish",
    "kikongo", "korean", "lao", "ligurian", "limburgish", "lingala", "lithuanian", "lombard",
    "latgalian", "luxembourgish", "luba-kasai", "ganda", "luo", "mizo", "standard latvian",
    "magahi", "maithili", "malayalam", "marathi", "minangkabau (arabic)", "minangkabau (latin)",
    "macedonian", "plateau malagasy", "maltese", "meitei (bengali)", "halh mongolian", "mossi",
    "maori", "burmese", "dutch", "norwegian nynorsk", "norwegian bokmål", "nepali", "northern sotho",
    "nuer", "nyanja", "occitan", "west central oromo", "odia", "pangasinan", "eastern punjabi",
    "papiamento", "western persian", "polish", "portuguese", "dari", "southern pashto",
    "ayacucho quechua", "romanian", "rundi", "russian", "sango", "sanskrit", "santali", "sicilian",
    "shan", "sinhala", "slovak", "slovenian", "samoan", "shona", "sindhi", "somali", "southern sotho",
    "spanish", "tosk albanian", "sardinian", "serbian", "swati", "sundanese", "swedish", "swahili",
    "silesian", "tamil", "tatar", "telugu", "tajik", "tagalog", "thai", "tigrinya",
    "tamasheq (latin)", "tamasheq (tifinagh)", "tok pisin", "tswana", "tsonga", "turkmen",
    "tumbuka", "turkish", "twi", "central atlas tamazight", "uyghur", "ukrainian", "umbundu",
    "urdu", "northern uzbek", "venetian", "vietnamese", "waray", "wolof", "xhosa", "eastern yiddish",
    "yoruba", "yue chinese", "chinese (simplified)", "chinese (traditional)", "standard malay",
    "zulu"]

    lan_nllb_codes = {
    "acehnese (arabic)": "ace_Arab", "acehnese (latin)": "ace_Latn", "mesopotamian arabic": "acm_Arab",
    "ta'izzi-adeni arabic": "acq_Arab", "tunisian arabic": "aeb_Arab", "afrikaans": "afr_Latn",
    "south levantine arabic": "ajp_Arab", "akan": "aka_Latn", "amharic": "amh_Ethi",
    "north levantine arabic": "apc_Arab", "modern standard arabic": "arb_Arab", "najdi arabic": "ars_Arab",
    "moroccan arabic": "ary_Arab", "egyptian arabic": "arz_Arab", "assamese": "asm_Beng",
    "asturian": "ast_Latn", "awadhi": "awa_Deva", "central aymara": "ayr_Latn", "south azerbaijani": "azb_Arab",
    "north azerbaijani": "azj_Latn", "bashkir": "bak_Cyrl", "bambara": "bam_Latn", "balinese": "ban_Latn",
    "belarusian": "bel_Cyrl", "bemba": "bem_Latn", "bengali": "ben_Beng", "bhojpuri": "bho_Deva",
    "banjar (arabic)": "bjn_Arab", "banjar (latin)": "bjn_Latn", "standard tibetan": "bod_Tibt",
    "bosnian": "bos_Latn", "buginese": "bug_Latn", "bulgarian": "bul_Cyrl", "catalan": "cat_Latn",
    "cebuano": "ceb_Latn", "czech": "ces_Latn", "chokwe": "cjk_Latn", "central kurdish": "ckb_Arab",
    "crimean tatar": "crh_Latn", "welsh": "cym_Latn", "danish": "dan_Latn", "german": "deu_Latn",
    "southwestern dinka": "dik_Latn", "dyula": "dyu_Latn", "dzongkha": "dzo_Tibt", "greek": "ell_Grek",
    "english": "eng_Latn", "esperanto": "epo_Latn", "estonian": "est_Latn", "basque": "eus_Latn",
    "ewe": "ewe_Latn", "faroese": "fao_Latn", "fijian": "fij_Latn", "finnish": "fin_Latn",
    "fon": "fon_Latn", "french": "fra_Latn", "friulian": "fur_Latn", "nigerian fulfulde": "fuv_Latn",
    "scottish gaelic": "gla_Latn", "irish": "gle_Latn", "galician": "glg_Latn", "guarani": "grn_Latn",
    "gujarati": "guj_Gujr", "haitian creole": "hat_Latn", "hausa": "hau_Latn", "hebrew": "heb_Hebr",
    "hindi": "hin_Deva", "chhattisgarhi": "hne_Deva", "croatian": "hrv_Latn", "hungarian": "hun_Latn",
    "armenian": "hye_Armn", "igbo": "ibo_Latn", "ilocano": "ilo_Latn", "indonesian": "ind_Latn",
    "icelandic": "isl_Latn", "italian": "ita_Latn", "javanese": "jav_Latn", "japanese": "jpn_Jpan",
    "kabyle": "kab_Latn", "jingpho": "kac_Latn", "kamba": "kam_Latn", "kannada": "kan_Knda",
    "kashmiri (arabic)": "kas_Arab", "kashmiri (devanagari)": "kas_Deva", "georgian": "kat_Geor",
    "central kanuri (arabic)": "knc_Arab", "central kanuri (latin)": "knc_Latn", "kazakh": "kaz_Cyrl",
    "kabiyè": "kbp_Latn", "kabuverdianu": "kea_Latn", "khmer": "khm_Khmr", "kikuyu": "kik_Latn",
    "kinyarwanda": "kin_Latn", "kyrgyz": "kir_Cyrl", "kimbundu": "kmb_Latn", "northern kurdish": "kmr_Latn",
    "kikongo": "kon_Latn", "korean": "kor_Hang", "lao": "lao_Laoo", "ligurian": "lij_Latn",
    "limburgish": "lim_Latn", "lingala": "lin_Latn", "lithuanian": "lit_Latn", "lombard": "lmo_Latn",
    "latgalian": "ltg_Latn", "luxembourgish": "ltz_Latn", "luba-kasai": "lua_Latn", "ganda": "lug_Latn",
    "luo": "luo_Latn", "mizo": "lus_Latn", "standard latvian": "lvs_Latn", "magahi": "mag_Deva",
    "maithili": "mai_Deva", "malayalam": "mal_Mlym", "marathi": "mar_Deva",
    "minangkabau (arabic)": "min_Arab", "minangkabau (latin)": "min_Latn", "macedonian": "mkd_Cyrl",
    "plateau malagasy": "plt_Latn", "maltese": "mlt_Latn", "meitei (bengali)": "mni_Beng",
    "halh mongolian": "khk_Cyrl", "mossi": "mos_Latn", "maori": "mri_Latn", "burmese": "mya_Mymr",
    "dutch": "nld_Latn", "norwegian nynorsk": "nno_Latn", "norwegian bokmål": "nob_Latn", "nepali": "npi_Deva",
    "northern sotho": "nso_Latn", "nuer": "nus_Latn", "nyanja": "nya_Latn", "occitan": "oci_Latn",
    "west central oromo": "gaz_Latn", "odia": "ory_Orya", "pangasinan": "pag_Latn",
    "eastern punjabi": "pan_Guru", "papiamento": "pap_Latn", "western persian": "pes_Arab", "polish": "pol_Latn",
    "portuguese": "por_Latn", "dari": "prs_Arab", "southern pashto": "pbt_Arab", "ayacucho quechua": "quy_Latn",
    "romanian": "ron_Latn", "rundi": "run_Latn", "russian": "rus_Cyrl", "sango": "sag_Latn",
    "sanskrit": "san_Deva", "santali": "sat_Olck", "sicilian": "scn_Latn", "shan": "shn_Mymr",
    "sinhala": "sin_Sinh", "slovak": "slk_Latn", "slovenian": "slv_Latn", "samoan": "smo_Latn",
    "shona": "sna_Latn", "sindhi": "snd_Arab", "somali": "som_Latn", "southern sotho": "sot_Latn",
    "spanish": "spa_Latn", "tosk albanian": "als_Latn", "sardinian": "srd_Latn", "serbian": "srp_Cyrl",
    "swati": "ssw_Latn", "sundanese": "sun_Latn", "swedish": "swe_Latn", "swahili": "swh_Latn",
    "silesian": "szl_Latn", "tamil": "tam_Taml", "tatar": "tat_Cyrl", "telugu": "tel_Telu",
    "tajik": "tgk_Cyrl", "tagalog": "tgl_Latn", "thai": "tha_Thai", "tigrinya": "tir_Ethi",
    "tamasheq (latin)": "taq_Latn", "tamasheq (tifinagh)": "taq_Tfng", "tok pisin": "tpi_Latn",
    "tswana": "tsn_Latn", "tsonga": "tso_Latn", "turkmen": "tuk_Latn", "tumbuka": "tum_Latn",
    "turkish": "tur_Latn", "twi": "twi_Latn", "central atlas tamazight": "tzm_Tfng", "uyghur": "uig_Arab",
    "ukrainian": "ukr_Cyrl", "umbundu": "umb_Latn", "urdu": "urd_Arab", "northern uzbek": "uzn_Latn",
    "venetian": "vec_Latn", "vietnamese": "vie_Latn", "waray": "war_Latn", "wolof": "wol_Latn",
    "xhosa": "xho_Latn", "eastern yiddish": "ydd_Hebr", "yoruba": "yor_Latn", "yue chinese": "yue_Hant",
    "chinese (simplified)": "zho_Hans", "chinese (traditional)": "zho_Hant", "standard malay": "zsm_Latn",
    "zulu": "zul_Latn"
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
            
            output_lan = lan_nllb_codes[option]

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
----------------------------------------------------------------------------   
                        Choose NLLB Model to Install
----------------------------------------------------------------------------   
1. nllb-200-distilled-600M - fastest, ~650 MB, 1-2 GB VRAM ({check_one})
2. nllb-200-distilled-1.3B - balanced, ~1.3 GB, 3-4 GB VRAM ({check_two})
3. nllb-200-3.3B - best quality, ~ 3 GB, 6-8 GB VRAM ({check_three})
  
0. Go back to more options 
----------------------------------------------------------------------------
                   
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

    broker = True
        
    while broker:

        option = input(f"""
---------------------------------------------------
            Update Computer Information
---------------------------------------------------                    
1. Automatic GPU update
2. Manual GPU update (for manual installations)

0. Go back to more options 
---------------------------------------------------
                   
""")
    
        print()

        if option == "1":

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

        elif option == "2":

            device_manual_choosing()

        elif option == "0":

            broker = False

        else:

            print("Enter a correct value (0-2)")
            input()

# Allows the user to manually change their GPU...

def device_manual_choosing():

    broker = True

    with open("cache/computer_information.pkl", "rb") as data:

        computer_information = pi.load(data)
        
    while broker:

        option = input(f"""
------------------------------
        Manual Update
------------------------------
Select the brand of your GPU

1. Nvidia
2. AMD/Ryzen
3. CPU 
                       
Choose CPU if GPU is not
capable enough (few VRAM)

0. Go back to more options
------------------------------
                   
""")
    
        print()

        broker = False

        if option == "1":

            computer_information["GPU"] = "nvidia"

            with open("cache/computer_information.pkl", "wb") as data:

                pi.dump(computer_information, data)

            print(f"GPU correctly updated to: {computer_information["GPU"]}")

        elif option == "2":
            
            computer_information["GPU"] = "amd"

            with open("cache/computer_information.pkl", "wb") as data:

                pi.dump(computer_information, data)

            print(f"GPU correctly updated to: {computer_information["GPU"]}")

        elif option == "3":

            computer_information["GPU"] = "cpu"

            with open("cache/computer_information.pkl", "wb") as data:

                pi.dump(computer_information, data)

            print(f"GPU correctly updated to: {computer_information["GPU"]}")

        elif option == "0":

            broker = False

        else:

            print("Enter a correct value (0-3)")
            input()

            broker = True

# ------------------------- Other Tools Menu -------------------------

def other_tools():

    broker = True
        
    while broker:

        option = input(f"""
--------------------------------------------------
                Other Tools - Menu
--------------------------------------------------                    
1. Cut specified input video
2. Concatenate input videos (merge multiple files)

0. Go back to more options 
--------------------------------------------------
                   
""")
    
        print()

        if option == "1":

            from modules import ffmpeg_handler as fh

            name = input("Enter the name of the video to cut (wihout extention): ")

            print()

            fh.cut_video(name)

        elif option == "2":

            from modules import ffmpeg_handler as fh

            fh.concatenate_video()

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