from importlib import import_module as im
from subprocess import run as sr
from urllib.request import urlretrieve as url_r
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
        
        print(f"This system is {system}. Installer.py is just available for windows atm")
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
        print(f"version: {library.version.__version__}")
        print()
    
    except AttributeError:

        print(f"version: {library.__version__}")
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

# ----------------------- Installing Visual C++ Redistributable updates ------------------------

    # Downloads and silently installs the latest version of Visual C++ Redistributable.
    # Also handles cases where it's already installed or a restart is required.

def update_vc_redist():

    print("Visual C++ Redistributable verification")
    
    restart_required = False

    # 1. Determine system architecture (x64 is the most common today)

    arch = "x64" if platform.machine().endswith('64') else "x86"
    
    # 2. URL for the latest version (aka.ms/vs/17/release/vc_redist.x64.exe is a direct link)

    url = f"https://aka.ms/vs/17/release/vc_redist.{arch}.exe"
    installer_path = "vcredist_temp.exe"

    try:

        # 3. Download the installer

        print(f"Downloading installer for {arch.upper()} architecture")
        url_r(url, installer_path)

        # 4. Run the installation SILENTLY.
        #    /quiet: Silent mode, no GUI.
        #    /norestart: Prevents automatic system restart after installation.

        print("Checking and then Installing/Updating Visual C++ if required")
        result = sr(
            [installer_path, '/quiet', '/norestart'],
            capture_output=True,
            text=True
        )

        # 5. Interpret the exit code.

        if result.returncode == 0:

            print("Visual C++ Redistributable installed/updated successfully.")
            print()

        elif result.returncode == 3010:

            # 3010 means installation was successful, BUT restart is required.

            print("⚠️ Installation completed, but a system restart is required.")
            print("Please restart your computer after installer.py executes")
            print("for the changes in Visual C++ Redistributable to take effect.")
            print("(Press enter to continue...)")
            input()

            restart_required = True

        elif result.returncode == 1638:

            # 1638 indicates a newer or equal version is already installed.
            print("Visual C++ Redistributable was already up to date.")
            print()

        else:

            # Any other error code.

            print(f"❌ Installation error. Code: {result.returncode}")
            print(f"   {result.stderr}")
            input()

        return restart_required

    except Exception as ae:
    
        print()
        print(f"❌ Error: {type(ae).__name__}: {ae}")
        print("Press Enter to exit...")
        input()

    finally:

        # 6. Clean up the temporary installer.

        if os.path.exists(installer_path):

            os.remove(installer_path)