import pickle as pi

# Identifies de device being used according to cache (nvidia, cpu, or amd)
# and verifies they are aviable, if not returns "cpu". Otherwise returns said device

def device_identifier():

    with open("cache/computer_information.pkl", "rb") as data:

        computer_information = (pi.load(data))
        gpu = computer_information["GPU"]

    if gpu == "nvidia":

        import torch

        # Cuda available check

        if torch.cuda.is_available():
            
            device = "cuda"

        else:

            device = "cpu"

            print()
            print("GPU not available, using CPU (slower)")

    elif gpu == "amd":

        import torch_directml

        if torch_directml.is_available():

            device = torch_directml.device()

        else:

            device = "cpu"

            print()
            print("GPU not available, using CPU (slower)")

    else:

        import torch 

        device = "cpu"

        print()
        print("not capable GPU registered in cache... If you have a GPU in your computer")
        print("Go to (6. More options...) and manage GPUs")

    return device