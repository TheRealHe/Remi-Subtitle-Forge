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

def print_languages_table(languages, columns=4):

    # Calculate max length of each name for alignment

    max_len = max(len(lang) for lang in languages) + 2
    
    import math

    # Calculate how many rows we need

    rows = math.ceil(len(languages) / columns)
    
    # Calculate total box width

    box_width = (max_len + 3) * columns + 2
    
    # Print top border

    print("╔" + "═" * (box_width - 2) + "╗")
    
    # Print centered title

    title = "AVAILABLE LANGUAGES"
    padding = (box_width - len(title) - 2) // 2
    print(f"║{' ' * padding}{title}{' ' * (box_width - len(title) - padding - 2)}║")
    
    # Separator line
    print("╠" + "═" * (box_width - 2) + "╣")
    
    # Print languages in columns

    for i in range(rows):

        row = ""

        for j in range(columns):

            idx = i + j * rows

            if idx < len(languages):

                lang = languages[idx]

                # Format each column left-aligned

                row += f"│ {lang:<{max_len - 1}}"

            else:

                row += "│" + " " * (max_len + 1)

        row += "│"
        print(row)
    
    # Print bottom border

    print("╚" + "═" * (box_width - 2) + "╝")