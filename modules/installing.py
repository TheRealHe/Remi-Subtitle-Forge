from importlib import import_module as im
from subprocess import run as sr
from shutil import rmtree as rmt
import sys
import platform
import ctypes
import os

# --------------------------- Install AI models and coverts them to ct2 ------------------------

def install_translation_model_ct2(AI_model, qua):

    print(f"Installing {AI_model} tokenaizer and model")
    print()

    from transformers import AutoTokenizer as at

    try: 

        check = sr(
            
            [sys.executable, '-m', "ctranslate2.converters.transformers", "--model", AI_model,
              "--output_dir", f"models/{AI_model}-ct2", "--quantization", qua],

            capture_output = True,
            text = True,
            timeout = 7200,
            
            )
                 
        print()
        print("Model compatible with ct2 Installed successfully")
        print()
        print("Starting with tokenaizer...")

        tokenizer = at.from_pretrained(

        AI_model,
        cache_dir = f"models/temp_folder/{AI_model}"

        )
       
        if check.returncode == 0:

            tokenizer.save_pretrained(f"models/{AI_model}-ct2")
                
            print(f"{AI_model} tokenaizer is now installed")
            print()

            print("Removing temporal files")

            rmt("models/temp_folder/")

            print("Removing was a success")
            print()

            # downloads specified tokenaizer in models/

            print(f"{AI_model} installing of tokenaizer and model was successful")
            print()

            return f"{AI_model}-ct2"

        else:
            
            error = check.stderr[:300] if check.stderr else "unknown error"
                
            print(f"{AI_model} could not be installed. Error: {error}...")
            print()

    except Exception as ae:
            
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        print("Press Enter to exit...")
        input()

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
            
            gpu = sr(
                
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
        
        check = sr(
            
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
        
        check = sr(
            
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

        commands = [sys.executable, "-m", "pip", "install"]

        for command in lib_term:

            commands.append(command)
    
        check = sr(
        
            commands,
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