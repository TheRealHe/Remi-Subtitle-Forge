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

ins.admin_permises()

# Checks that the current python running the program is a compatible version

print("Python Check")

print(f"Python version is: {sys.version}")

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

# I may add this later on...

def AI_GPU_installation():

    if gpu == "nvidia":

        try:
        
            import torch 
        
            print(f"Torch already Installed")
            print(torch.__version__)
        
            if torch.cuda.is_available():
            
                gpu_name = torch.cuda.get_device_name()
            
                print(f"Nvidia GPU available: {gpu_name}")
                print()
            
            else: 
            
                print("Not Nvidia GPU available")
                print("Try updating Nvidia drivers")
                print()
            
        except ImportError:
        
            print("Torch not installed")
            print()
            
            print("Installing Torch for Nvidia")
            print()
            
            try:
                
                check = sr(
                    
                    [sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio", "--index-url", "https://download.pytorch.org/whl/cu118"],
                    capture_output = True,
                    text = True,
                    timeout = 1200

                )
                
                if check.returncode == 0:
                    
                    import torch 
        
                    print(f"Torch for Nvidia GPU Installed")    
                    print(torch.__version__)
                
                    if torch.cuda.is_available():
                    
                        gpu_name = torch.cuda.get_device_name() 
                    
                        print(f"Nvidia GPU available: {gpu_name}")
                        print()
                    
                    else: 
                    
                        print("Not Nvidia GPU available")
                        print("Try updating Nvidia drivers")
                        print()
                        
                else:
                
                    error = check.stdout[:300] if check.stdout else "unknown error"
                    
                    print(f"Torch for Nvidia GPU could not be installed. Error: {error}...")
                    print()
                        
            except Exception as ae:
        
                print()
                print(f"❌ Error: {type(ae).__name__}: {ae}")
                print("Press Enter to exit...")
                input()

        except Exception as ae:
        
            print()
            print(f"❌ Error: {type(ae).__name__}: {ae}")
            print("Press Enter to exit...")
            input()
            
    elif gpu == "amd":
        
        try:
        
            import directml
            
            print("Torch DirecTML (amd) already installed")
            print(directml.__version__)
            print()
            
        except ImportError:
            
            print("Torch not installed")
            print()
            
            print("Installing Torch for AMD (DirecTML)")
            print()
            
            try:
                
                check = sr(
                    
                    [sys.executable, "-m", "pip", "install", "torch-directml"],
                    capture_output=True,
                    text=True,
                    timeout=1200 
                    
                )
                
                if check.returncode == 0:
                    
                    print("Torch DirecTML (amd) successfully installed")
                    
                    import directml
                    
                    print(directml.__version__)
                    print()
                    
                else:
                
                    error = check.stdout[:300] if check.stdout else "unknown error"
                    
                    print(f"Torch DirecTML (amd) could not be installed. Error: {error}...")
                    print()
                
            except Exception as ae:
            
                print()
                print(f"❌ Error: {type(ae).__name__}: {ae}")
                print("Press Enter to exit...")
                input()
                
    else:
        
        try:
            
            import torch
            
            print(f"Torch already Installed")
            print(torch.__version__)
            
        except ImportError:
        
            print("Torch not installed")
            print()
            
            print("Installing Torch for CPU")
            print()
        
            try:
            
                check = sr(
                        
                        [sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio"],
                        capture_output = True,
                        text = True,
                        timeout = 1200

                    )
                    
                if check.returncode == 0:
                        
                    print("Torch for CPU Installed Successfully")
                    
                    import torch
                    
                    print(torch.__version__)
                    print()
                
                else:
                    
                    error = check.stdout[:300] if check.stdout else "unknown error"
                    
                    print(f"Torch for CPU could not be installed. Error: {error}...")
                    print()
                
            except Exception as ae:
            
                print()
                print(f"❌ Error: {type(ae).__name__}: {ae}")
                print("Press Enter to exit...")
                input()
            
        
# Saves computer information in .pkl
                        
with open("cache/computer_information.pkl", "wb") as data:

    com_info = {

        "GPU": gpu,
        "PYTHON_VERSION": f"3.{sys.version_info.minor}"

    }

    pi.dump(com_info, data)
    
print("Installation Complete Successfully")
print("Press Enter to exit...")
input()

