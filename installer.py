# This script verifies if programs needed to run are installed or not.
# If they are not it installs them (Just working in windows 10+ for now)

import sys
import os
import subprocess
import platform
import ctypes
from importlib import import_module as im

# ---------------------------------- Give admin permises to the script ------------------------

def admin_permises():

    is_admin = False
    
    try:
        
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    
    except:
        
        is_admin = False
        
    if not is_admin:
        
        print("Program needs to be run as administrator")
        print("Re-starting as an administrator")
        print()
        
        install_path = f'"{sys.executable}"'
        safe_args = " ".join(([f'"{arg}"' for arg in sys.argv]))
        
        check = ctypes.windll.shell32.ShellExecuteW(
            
            None,                 
            "runas",              
            install_path,       
            safe_args,   
            None,                 
            1                     
        )
        
        if check <= 32:
            
            print("Failed to get administrator privileges.")
            print("Please run this script as Administrator.")
            print("Press Enter to exit...")
            input()
            
            sys.exit(1)
        
        sys.exit(0)
        
    print("Executing as administrator")
    print()
        

# ---------------------------------- Detects the GPU in the computer ------------------------

def gpu_detecter():
    
    # Identiry the OS of the computer
    
    system = platform.system()
    
    print("Looking for GPUs")
    
    if system == "Windows":
        
        try:
            
            # If it is windows, it runs a cmd check
            
            gpu = subprocess.run(
                
                ["wmic", "path", "win32_VideoController", "get", "name"],
                capture_output = True,
                text = True,
                timeout = 20
                
                )
            
            # Runs if command goes well
            
            if gpu.returncode == 0:
                
               lines = gpu.stdout.split("\n")
               lines.remove(lines[0])

               GPUs = []
               
               # Get the GPU names
               
               for line in lines:
               
                    if line != "":
                       
                        line = line.strip()
                        line = line.upper()
                        
                        GPUs.append(line)
                        
                        print(f"GPU: {line} Found")
            
                # Read names and gets the best GPU
            
               for GPU in GPUs:
                    
                    if "NVIDIA" in GPU and ("GEFORCE" in GPU or "QUADRO" in GPU or "TESLA" in GPU ):
                        
                        print(f"The {GPU} will be used")
                        print()
                    
                        return "nvidia"
                    
                    elif ("AMD" in GPU or "RADEON" in GPU) and not ("VEGA" in GPU and not ("RX" in GPU)) and not ("GRAPHICS" in GPU):
                    
                        print(f"The {GPU} will be used")
                        print()    
                            
                        return "amd"
                        
               print("GPUs were not found. Using CPU therefore.")
               print()
                                
               return "cpu"
                                
        except Exception as ae:
    
            print()
            print(f"❌ Error: {type(ae).__name__}: {ae}")
            print("Press Enter to exit...")
            input()
            
    else:
        
        print(f"This system is {system}. The program is just available for windows atm")
        print()

# ---------------------------------- Installing APPs with Funct ------------------------

def check_app(app_term, app, version_check):

    try:
        
        print(f"{app} Check")
        
        check = subprocess.run(
            
        [app_term, version_check], 
        capture_output = True, 
        text = True, 
        timeout = 5
        ) 
        
        if check.returncode == 0:
            
            print(f"{app} already installed")
            print((check.stdout.split('\n'))[0])
            print()
        
    except FileNotFoundError:

        install_app(app, app_term, version_check)

    except Exception as ae:
        
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        print("Press Enter to exit...")
        input()

def install_app(app, app_term, version_check):
        
    print(f"{app} not installed")
    print()
        
    # Installing app with winget
        
    print(f"Installing {app}")
        
    try:
        
        check = subprocess.run(
            
            ["winget", "install", app],
            capture_output = True,
            text = True,
            timeout = 300,
        )
            
        if check.returncode == 0:
                
            print(f"{app} installed successfully")
                
            check_app(app, app_term, version_check)

        else:
            
            error = check.stderr[:300] if check.stderr else "unknown error"
            
            print(f"{app} could not be installed. Error: {error}...")
            print()

    except Exception as ae:
        
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        print("Press Enter to exit...")
        input()

# ---------------------------------- Installing Libraries with Funct ------------------------

def check_lib(lib, lib_term):

    print(f"{lib} Check")

    try:
        
        library = im(lib)
            
        print(f"{lib} already installed")
        print(library.version.__version__)
        print()
    
    except AttributeError:

        print(library.__version__)
        print()

    except ImportError:
        
        print(f"{lib} not installed")
        print()

        install_lib(lib, lib_term)

def install_lib(lib, lib_term):

    print(f"Installing {lib}")
    
    try:
    
        check = subprocess.run(
        
            [sys.executable, "-m", "pip", "install", lib_term],
            capture_output = True,
            text = True,
            timeout = 300,
        )
        
        if check.returncode == 0:
            
            print(f"{lib} installed successfully")
            
            library = im(lib)
            
            print(library.version.__version__)
            print()

            check_lib(lib, lib_term)
            
        else:
            
            error = check.stderr[:300] if check.stderr else "unknown error"
            
            print(f"{lib} could not be installed. Error: {error}...")
            print()
            
    except Exception as ae:
    
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        print("Press Enter to exit...")
        input()

# ---------------------------------------- Main Starts -------------------------------------

print()
print("Starting Installer...")
print()

admin_permises()

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
                        
        check_app("choco", "Chocolatey.Chocolatey", "-v")
            
        print("Installing compatible Python")
        print()
            
        py_get = subprocess.run(
            
            ["choco", "install", "python", "-y"],
            capture_output = True,
            text = True,
            timeout = 300,
            
        )
            
        # Checking it was properly installed
            
        if py_get.returncode == 0:
                    
            # Running the script again with compatible version of python
                    
            try:
            
                re_run = subprocess.run(
                            
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
    
check_app("ffmpeg", "ffmpeg", "-version")
    
# Checks if library is already installed, If not Installs it.

check_lib("yt_dlp", "yt_dlp")
check_lib("whisper", "openai-whisper")
check_lib("whisper_timestamped", "whisper-timestamped")
check_lib("ctranslate2", "ctranslate2")
check_lib("transformers", "transformers")
check_lib("silero_vad", "silero-vad")
check_lib("onnxruntime", "onnxruntime")

# Creating NLLB structure

if os.path.exists("models"):

    print("NLLB structure already exists")
    print()

else:

    os.mkdir("models")

# Checking GPUs

gpu = gpu_detecter()

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
                
                check = subprocess.run(
                    
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
                
                check = subprocess.run(
                    
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
            
                check = subprocess.run(
                        
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
            
        
# Saves information in .txt
                        
with open("cache/computer_information.txt", "w") as data:
                        
    data.write(f"PYTHON_VERSION: 3.{sys.version_info.minor}\n")
    data.write(f"GPU: {gpu}\n")
    
print("Installation Complete Successfully")
print("Press Enter to exit...")
input()

