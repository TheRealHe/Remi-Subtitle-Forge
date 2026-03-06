import ctranslate2 as ct
from transformers import AutoTokenizer as at
import torch
import os

# Global variables to corroborate lazy loading

tokenizer = None
model = None

# Function that translate the Spanish .srt file to English

def srt_translation(srt_file_name):

    global tokenizer
    global model

    if not (os.path.exists(f"spanish_subtitles/{srt_file_name}.srt")):

        print()
        print(".srt not found")
        input()
        
        return None

    # Source and Final language being defined

    source_lang = "spa_Latn"
    final_lang = "eng_Latn"

    # Cuda available check

    if torch.cuda.is_available():
        
        device = "cuda"

    else:

        device = "cpu"

        print("GPU not available, using CPU (slower)")

    # Loads tokenizer if needed

    if tokenizer == None:

        try:

            tokenizer = at.from_pretrained(

                "facebook/nllb-200-distilled-600M",

                src_lang = source_lang,

                local_files_only = True

            )

        # In case device has not access to internet. Runs function fully offline

        except ConnectionError:

            os.environ["HF_HUB_OFFLINE"] = "1"
            os.environ["TRANSFORMERS_OFFLINE"] = "1"
            os.environ["HF_DATASETS_OFFLINE"] = "1"
            os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"

            from transformers import AutoTokenizer as AT

            tokenizer = AT.from_pretrained(

                "facebook/nllb-200-distilled-600M",

                src_lang = source_lang,

                local_files_only = True

            )

    # Loads model if needed

    if model == None:
        
        model = ct.Translator(

        "cache/nllb-600M-ct2",
        device = device,
        compute_type = "int8"

        )

    # Reading and translating lines from spanish .srt

    with open(f"spanish_subtitles/{srt_file_name}.srt", "r") as spanish_subtitles:

        lines = spanish_subtitles.readlines()

        translated_lines = []

        for line in lines:

            if (line[0].isdigit() == False) and (line != ""):
                
                try:

                    translated_line = model_token_flow(line, final_lang)

                    translated_lines.append(f"{translated_line}\n")

                except Exception as ae:

                    print()
                    print(f"❌ Error: {type(ae).__name__}: {ae}")
                    input()

                    return None

            else:

                if line == "":

                    translated_lines.append("\n")

                else:

                    translated_lines.append(line)

    # Writes the translated lines in a new .srt english subtitles document

    with open(f"english_subtitles/{srt_file_name}.srt", "w") as english_subtitles:

        for translated_line in translated_lines:

            english_subtitles.write(f"{translated_line}")

def model_token_flow(text, final_lang):

    # Encode incoming text

    tokens = tokenizer.tokenize(text)
    print(tokens)

    # Model translates tokens
    # There may be an Issue with visual C++. If that is the case, installing
    # redistributable version recommended.

    translation = model.translate_batch(

        [tokens],
        target_prefix = [[final_lang]],
        max_decoding_length = 10,
        repetition_penalty = 1.5,
        prefix_bias_beta = 0.5,
    )

    print(translation[0])

    # Saves the best translation tokens

    translated_tokens = translation[0].hypotheses[0]
    print(translated_tokens)

    # Decode the tokens to actual text

    translated_text = tokenizer.convert_tokens_to_string(translated_tokens)

    return translated_text
