<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]
  [![Unlicense License][license-shield]][license-url]
  
  [![LinkedIn][linkedin-shield]][linkedin-url]

</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Remi Subtitle Forge</h3>

  <p align="center">
    A complete pipeline to generate subtitles with Whisper (+100 languages), translate them with NLLB-200 (+200 languages), and burn specified subtitles into input videos.
    <br />
    <a href="https://github.com/TheRealHe/Remi-Subtitle-Forge"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#usage">View Demo</a>
    &middot;
    <a href="https://github.com/TheRealHe/Remi-Subtitle-Forge/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/TheRealHe/Remi-Subtitle-Forge/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation-automatic--recommended">Installation (Automatic – Recommended)</a></li>
        <li><a href="#manual-installation-linux--macos">Manual Installation (Linux / macOS)</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#main-menu">Main Menu</a></li>
        <li><a href="#more-options-menu">More Options Menu</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#support-the-project">Support the Project</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project automates the entire workflow of generating burned-in subtitles for videos, supporting translation between any of the +200 languages supported by NLLB and transcription of any of the +100 languages supported by Whisper. It was designed for content creators, translators, or anyone who needs to repurpose videos for a global audience.

**Why this project exists?**
- Whisper is great for transcription, but needs post-processing for proper subtitle formatting (.srt).
- NLLB-200 provides high-quality translation among +200 languages.
- Hardcoded (burned-in) subtitles are part of the video image itself, so they work on any device or player (TV, smartphone, projector, etc.) without needing separate .srt files or player support.
- Human-in-the-loop – Automatically generated .srt files can be edited by the user at any stage, allowing manual correction of transcription or translation errors before burning them into the final video.

**What makes it special?**

- **Auto‑installer** – Checks and installs Python 3.8+, FFmpeg, PyTorch (among other dependencies), and automatically downloads AI models.
- **Fully dynamic configuration** – Everything is configurable through interactive menus:
  - **Translation models** – Install and switch between NLLB sizes (600M, 1.3B, 3.3B) on the fly.
  - **Whisper models** – Choose between tiny, base, small, medium, large, or turbo based on your VRAM.
  - **Input/Output languages** – Select from +100 languages for transcription (Whisper) and +200 languages for translation (NLLB).
  - **Subtitling task** – Burn either the original transcription OR the translated version.
  - **Subtitle formatting** – Adjust maximum subtitle duration and lines per subtitle.
- **Human-in-the-loop workflow** – Since .srt files are plain text, users can manually correct any transcription or translation errors using any text editor before burning them into the video. This ensures final subtitle quality even when automatic generation makes mistakes.
- **Modular design** – Each step (download, transcription, translation, burning, cleanup) runs independently or in sequence.
- **Interactive menu** – Execute single steps (e.g., 2) or a range (e.g., 2,4 to run steps 2,3,4).
- **Smart SRT generation** – Respects a maximum subtitle duration, and lines per subtitle parameters.
- **Video preprocessing tools** – Cut videos by time, concatenate multiple videos, and automatically avoid file overwrites with unique naming.
- **Cross‑platform GPU support** – Works with NVIDIA (CUDA) and AMD (DirectML), with automatic fallback to CPU.
- **Persistent configuration** – All settings are saved in cache/settings.pkl and persist between sessions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.org]][Python-url]
* [![PyTorch][PyTorch.org]][PyTorch-url]
* [![Whisper][Whisper]][Whisper-url]
* [![NLLB][NLLB]][NLLB-url]
* [![FFmpeg][FFmpeg.org]][FFmpeg-url]
* [![yt-dlp][yt-dlp]][yt-dlp-url]
* [![ONNX Runtime][onnxruntime-shield]][onnxruntime-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- **Windows 10/11** (the auto‑installer is Windows‑only; other OS may work with manual setup)
- **Python 3.8+** Required for compatibility with modern ML libraries (Transformers, CTranslate2, etc.). Your existing Python version will be verified by installer.py.
- **Administrator privileges** (required for the installer to set up FFmpeg and Chocolatey)
- **Internet connection** (to download models and dependencies)

### Installation (Automatic – Recommended)

1. **Clone the repository**
```sh
   git clone https://github.com/your_username/Remi-Subtitle-Forge.git
   cd Remi-Subtitle-Forge
```
2. **Run the installer**
```sh
    python installer.py
```
    
**The installer will:**

- Request administrator privileges
- Install FFmpeg via winget
- Install all Python dependencies (whisper‑timestamped, torch, ctranslate2, yt‑dlp, etc.)
- Detect your GPU (NVIDIA, AMD, or CPU) and install the correct PyTorch backend
- Download the NLLB‑200 model (converted to CTranslate2) and prepare Whisper model (small) for download just before first use

### Manual Installation (Linux / macOS)

f you are not using Windows, or if the automatic installer fails, you can install everything manually.

**All dependencies and detailed instructions are documented in:**

[DEPENDENCIES.md](DEPENDENCIES.md)

**This file includes:**

- Python version requirements (3.8+)
- List of all required Python packages with installation commands
- System dependencies (FFmpeg, etc.) for Linux and macOS
- GPU backend setup (CUDA for NVIDIA, DirectML for AMD, or CPU fallback)
- Model download instructions (Whisper and NLLB-200)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Main Menu

After installation, run the main menu:
```sh
python main.py
```
You will see an interactive terminal menu:
```sh
--------------------------------------------------------------------------
                    Terminal Menu - Subtitle generator
--------------------------------------------------------------------------                 
1. Download video from YouTube.
2. Create video transcription (.str file) in [current input language]
3. Translate transcription (.str file) to [current output language]
4. Burn translated subtitles into de original video
5. Delete specified subtitles (.srt files) and input video
6. More options...
  
0. close the program. 
--------------------------------------------------------------------------
(It is possible to run a range of steps. For example: 2,4 will run steps: 2,3,4)
```

**All** generated files are stored in dedicated folders:

- input_videos/ – input videos
- transcripted_subtitles/ – generated transcription .srt
- translated_subtitles/ – translated transcription .srt
- output_videos/ – final videos with burned‑in subtitles

### More Options Menu

```sh
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
```

**Options Description:**

| Command | What it does |
|---------|---------------|
| `1` | **Manage languages Change the input language** - (for Whisper transcription) and output language (for NLLB translation). |
| `2` | **Manage AI translation models** - Install, switch between, or delete NLLB translation models (600M, 1.3B, 3.3B). |
| `3` | **Change Whisper parameters** - Adjust the Whisper model size (tiny to turbo), maximum subtitle duration (seconds), and lines per subtitle. |
| `4` | **Change subtitulation task** - Choose which subtitles get burned into the final video: transcribed (original language) or translated (target language). |
| `5` | **Update computer information in cache** - Manually select which GPU the AI should use (if multiple GPUs are available). |
| `6` | **Other tools** - Allow the user to cut videos by time or concatenate multiple videos before processing. |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Core pipeline (download, transcribe, translate, burn, cleanup) 
- [x] Auto‑installer for dependencies and models 
- [x] Interactive menu with range execution  
- [x] Smart SRT splitting (time‑aware)  
- [x] Multi‑language support (target other languages)  
- [ ] Add a simple GUI (optional)  
- [ ] Publish to PyPI  

See the open issues for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Support the Project

If you find this tool useful, consider supporting its development:

[![Support via Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://patreon.com/DaanDev)

<!-- LICENSE -->
## License

Distributed under the Unlicense License. See [LICENSE.txt](LICENSE.txt) for more information.

<!-- CONTACT -->
## Contact

Daniel Rojas - hdrojas.sanin@gmail.com - [LinkedIn][linkedin-url]

Project Link: [https://github.com/TheRealHe/Remi-Subtitle-Forge](https://github.com/TheRealHe/Remi-Subtitle-Forge)


<!-- ACKNOWLEDGMENTS -->
<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [OpenAI Whisper](https://github.com/openai/whisper)
* [Whisper Timestamped](https://github.com/linto-ai/whisper-timestamped)
* [NLLB-200](https://github.com/facebookresearch/fairseq/tree/nllb)
* [CTranslate2](https://github.com/OpenNMT/CTranslate2)
* [FFmpeg](https://ffmpeg.org)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [PyTorch](https://pytorch.org)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [ONNX-Runtime](https://github.com/microsoft/onnxruntime) 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/TheRealHe/spanish_to_english_subtitles_generator.svg?style=for-the-badge
[contributors-url]: https://github.com/TheRealHe/spanish_to_english_subtitles_generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TheRealHe/spanish_to_english_subtitles_generator.svg?style=for-the-badge
[forks-url]: https://github.com/TheRealHe/spanish_to_english_subtitles_generator/network/members
[stars-shield]: https://img.shields.io/github/stars/TheRealHe/spanish_to_english_subtitles_generator.svg?style=for-the-badge
[stars-url]: https://github.com/TheRealHe/spanish_to_english_subtitles_generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/TheRealHe/spanish_to_english_subtitles_generator.svg?style=for-the-badge
[issues-url]: https://github.com/TheRealHe/spanish_to_english_subtitles_generator/issues
[license-shield]: https://img.shields.io/github/license/TheRealHe/spanish_to_english_subtitles_generator.svg?style=for-the-badge
[license-url]: https://github.com/TheRealHe/spanish_to_english_subtitles_generator/blob/master/LICENSE
[product-screenshot]: images/screenshot.png

[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org
[PyTorch.org]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[PyTorch-url]: https://pytorch.org
[Whisper]: https://img.shields.io/badge/Whisper-FFD43B?style=for-the-badge&logo=openai&logoColor=black
[Whisper-url]: https://github.com/openai/whisper
[NLLB]: https://img.shields.io/badge/NLLB-2563EB?style=for-the-badge&logo=meta&logoColor=white
[NLLB-url]: https://github.com/facebookresearch/fairseq/tree/nllb
[FFmpeg.org]: https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white
[FFmpeg-url]: https://ffmpeg.org
[yt-dlp]: https://img.shields.io/badge/yt--dlp-FF0000?style=for-the-badge&logo=youtube&logoColor=white
[yt-dlp-url]: https://github.com/yt-dlp/yt-dlp
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/daandev/
[onnxruntime-shield]: https://img.shields.io/badge/ONNX%20Runtime-717272?style=for-the-badge&logo=onnx&logoColor=white
[onnxruntime-url]: https://onnxruntime.ai
