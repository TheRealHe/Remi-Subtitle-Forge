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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][[linkedin-url](https://www.linkedin.com/in/daandev/)]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Automatic Spanish to English Subtitles Generator</h3>

  <p align="center">
    A complete pipeline to generate Spanish subtitles, translate them to English, and burn them into videos.
    <br />
    <a href="https://github.com/your_username/automatic_spanish_to_english_subtitles"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#usage">View Demo</a>
    &middot;
    <a href="https://github.com/your_username/automatic_spanish_to_english_subtitles/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/your_username/automatic_spanish_to_english_subtitles/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project automates the entire workflow of generating hardcoded (burned-in) English subtitles for Spanish videos. It was designed for content creators, translators, or anyone who needs to repurpose Spanish videos for an English-speaking audience.

**Why this project exists?**
- Whisper is great for transcription, but needs post-processing for proper subtitle formatting (`.srt`).
- NLLB-200 provides high-quality translation between Spanish and English, even for "low-resource" expressions.
- Burning subtitles into videos ensures compatibility with any media player (no external files or players needed).

**What makes it special?**
- **Auto‑installer** – Checks and installs Python 3.11, FFmpeg, PyTorch (with GPU support), and even downloads the AI models automatically.
- **Modular design** – Each step (download, transcription, translation, burning, cleanup) runs independently or in sequence.
- **Interactive menu** – Execute single steps (e.g., `2`) or a range (e.g., `2,4` to run steps 2,3,4).
- **Smart SRT generation** – Groups Whisper words into lines, respects a maximum subtitle duration, and splits long segments cleanly.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.org]][Python-url]
* [![PyTorch][PyTorch.org]][PyTorch-url]
* [![Whisper][Whisper]][Whisper-url]
* [![NLLB][NLLB]][NLLB-url]
* [![FFmpeg][FFmpeg.org]][FFmpeg-url]
* [![yt-dlp][yt-dlp]][yt-dlp-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- **Windows 10/11** (the auto‑installer is Windows‑only; other OS may work with manual setup)
- **Administrator privileges** (required for the installer to set up FFmpeg and Chocolatey)
- **Internet connection** (to download models and dependencies)

### Installation (Automatic – Recommended)

1. **Clone the repository**
```sh
   git clone https://github.com/your_username/automatic_spanish_to_english_subtitles.git
   cd automatic_spanish_to_english_subtitles
```
2. **Run the installer**
```sh
    python installer.py
```
    
The installer will:

- Request administrator privileges
- Install FFmpeg via winget
- Install all Python dependencies (whisper‑timestamped, torch, ctranslate2, yt‑dlp, etc.)
- Detect your GPU (NVIDIA, AMD, or CPU) and install the correct PyTorch backend
- Download the Whisper model (small) and the NLLB‑200 model (converted to CTranslate2)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

After installation, run the main menu:
```sh
python main.py
```
You will see an interactive terminal menu:
```sh
--------------------------------------------------------------------------
                    Terminal Menu - Subtitle generator
--------------------------------------------------------------------------                 
1. Download Video from YouTube.
2. Create spanish transcription (.srt file) of the selected video.
3. Translate Spanish transcription (.srt file) to English
4. Burn the translated subtitle into the original video
5. Delete specified subtitles (.srt files) and input video
6. More options...

0. close the program. 
--------------------------------------------------------------------------
(It is possible to run a range of steps. For example: 2,4 will run steps: 2,3,4)
```

Typical workflow examples:

| Command | What it does |
|---------|---------------|
| `1` | Download a video from YouTube |
| `2` | Generate Spanish subtitles (`.srt`) |
| `3` | Translate Spanish `.srt` to English |
| `4` | Burn subtitles into the video |
| `5` | Delete original video and subtitle files |
| RANGES `2,4` (FOR EXAMPLE) | Run steps 2, 3, 4 in one go |

All generated files are stored in dedicated folders:

- videos/ – input videos
- spanish_subtitles/ – generated Spanish .srt
- english_subtitles/ – translated English .srt
- subtitled_videos/ – final videos with burned‑in English subtitles

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Core pipeline (download, transcribe, translate, burn, cleanup) 
- [x] Auto‑installer for dependencies and models 
- [x] Interactive menu with range execution  
- [x] Smart SRT splitting (time‑aware)  
- [ ] Multi‑language support (target other languages)  
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

<!-- LICENSE -->
## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Daniel Rojas - hdrojas.sanin@gmail.com - [![LinkedIn][linkedin-shield]][[linkedin-url](https://www.linkedin.com/in/daandev/)]

Project Link: [https://github.com/TheRealHe/spanish_to_english_subtitles_generator](https://github.com/TheRealHe/spanish_to_english_subtitles_generator)


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

