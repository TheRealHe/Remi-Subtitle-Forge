# This script verifies if programs needed to run are installed or not.
# If they are not it installs them (Just working in windows 10+ for now)

import sys
import os
import pickle as pi
from subprocess import run as sr
from modules import installing as ins

# ---------------------------------------- Main Starts -------------------------------------

print()
print("Starting Installer...")
print()

# Gets admin permises

ins.admin_permises()

# Installs/updates Visual c++ Redistributable

restart_required = ins.update_vc_redist()

# Checks that the current python running the program is a compatible version

print("Python Check")

print(f"Python version is: {((sys.version).split(" "))[0]}")

if (sys.version_info.major >= 3) and (sys.version_info.minor >= 8):

    print("Current Python is compatible")
    print()
    
else: 
    
    print("Current Python is not compatible")
        
    # Installing last version of python
        
    try:
                        
        ins.check_app("choco", "Chocolatey.Chocolatey", "-v")
            
        print("Installing compatible Python")
        print()
            
        py_get = sr(
            
            ["choco", "install", "python", "-y"],
            capture_output = True,
            text = True,
            timeout = 300,
            
        )
            
        # Checking it was properly installed
            
        if py_get.returncode == 0:
                    
            # Running the script again with compatible version of python
                    
            try:
            
                re_run = sr(
                            
                ["python", "installer.py"],
                capture_output = True,
                text = True,
                timeout = 1200   
                            
                )
                        
                sys.exit(re_run.returncode)
                        
            except Exception as ae:
                        
                print()
                print(f"❌ Error: {type(ae).__name__}: {ae}")
                print("Press Enter to exit...")
                input()
                
        else:
                
            error = py_get.stdout[:300] if py_get.stdout else "unknown error"
                
            print(f"Compatible Python could not be Installed. Error: {error}...")
            print()
        
        
    except Exception as ae:
            
            print()
            print(f"❌ Error: {type(ae).__name__}: {ae}")
            print("Press Enter to exit...")
            input()

            sys.exit(1)
    
# Checks if app is already installed, If not Installs it.
    
ins.check_app("ffmpeg", "ffmpeg", "-version")
    
# Checks if library is already installed, If not Installs it.

ins.check_lib("yt_dlp", ["yt_dlp"])
ins.check_lib("whisper", ["openai-whisper"])
ins.check_lib("whisper_timestamped", ["whisper-timestamped"])
ins.check_lib("ctranslate2", ["ctranslate2"])
ins.check_lib("transformers", ["transformers"])
ins.check_lib("silero_vad", ["silero-vad"])
ins.check_lib("onnxruntime", ["onnxruntime"])

# Creating NLLB structure

if os.path.exists("models"):

    print("NLLB structure already exists")
    print()

else:

    os.mkdir("models")

    # installing facebook/nllb-200-distilled-600M model and tokenaizer

    ins.install_translation_model_ct2("facebook/nllb-200-distilled-600M", "int8")

# Checking GPUs

gpu = ins.gpu_detecter()

# ---------------------------- Installing AI Drivers for selected GPU ------------------------

if gpu == "nvidia":

    print("This PC requires Torch for Nvidia...")

    ins.check_lib("torch", ["torch", "torchvision", "torchaudio", "--index-url", "https://download.pytorch.org/whl/cu118"])

elif gpu == "amd":

    print("This PC requires Torch for AMD...")

    ins.check_lib("torch_directml", ["torch-directml"])

else:

    print("This PC requires Torch for CPU...")

    ins.check_lib("torch", ["torch", "torchvision", "torchaudio", "--index-url", "https://download.pytorch.org/whl/cpu"])
         
        
# Saves computer information in .pkl
                        
with open("cache/computer_information.pkl", "wb") as data:

    com_info = {

        "GPU": gpu,
        "PYTHON_VERSION": f"{((sys.version).split(" "))[0]}"

    }

    pi.dump(com_info, data)

if restart_required:

    print("⚠️ IMPORTANT: A system restart is required for Visual C++ to work.")
    print("Please restart your computer before using the program (main.py).")
    print()

    
print("Installation Complete Successfully")
print("Press Enter to exit...")
input()