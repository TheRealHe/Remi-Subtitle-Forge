## Dependencies

This project requires the following main libraries/APPs:

| Library | Purpose | Installation |
|---------|---------|--------------|
| **ONNX Runtime** | ML model inference accelerator by Microsoft. Significantly speeds up the Voice Activity Detection (Silero VAD) used by Whisper. | `pip install onnxruntime` |
| **Whisper** | Speech-to-text transcription model by OpenAI. Converts audio to [input language] text with word-level timestamps. | `pip install openai-whisper` |
| **whisper-timestamped** | Extension of Whisper that provides more accurate word timestamps and integrates Silero VAD for silence detection. | `pip install whisper-timestamped` |
| **CTranslate2** | Fast inference engine for Transformer models. Used to run the NLLB translation model efficiently on CPU. | `pip install ctranslate2` |
| **Transformers** | Hugging Face library for loading and using pre-trained models like NLLB-200. | `pip install transformers` |
| **Silero VAD** | Voice Activity Detection model that identifies speech segments in audio. Helps Whisper avoid transcribing silence. | `pip install silero-vad` |
| **PyTorch** | Deep learning framework used as backend for Whisper, Silero VAD, and Transformers. | `pip install torch torchaudio` |
| **yt-dlp** | YouTube downloader library. Installs video from YouTube videos. | `pip install yt-dlp` |
| **FFmpeg** | Multimedia framework for processing audio and video. Used for audio extraction and burning subtitles into videos. | Install via winget: `winget install ffmpeg` |

### PyTorch Installation (GPU/CPU)

The correct PyTorch version depends on your GPU. The auto-installer handles this automatically, but for manual installation:

| GPU Type | Command |
|---------|---------|
| NVIDIA GPU (CUDA) | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118` |
| AMD GPU (DirectML) | `pip install torch-directml` |
| No GPU / Low VRAM (CPU) | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu` |

**Note:** If you have an older NVIDIA GPU (Compute Capability < 3.5), the CPU version is recommended.

**After installing PyTorch, the version of it being used MUST be entered into the program**

This is possible in the **Update Computer Information** menu, found in the **More options...** menu:

```sh
---------------------------------------------------
            Update Computer Information
---------------------------------------------------                    
1. Automatic GPU update
2. Manual GPU update (for manual installations)

0. Go back to more options 
---------------------------------------------------
```

After getting in this menu **select option 2**, and choose the correct option for your hardware:

```sh
------------------------------
        Manual Update
------------------------------
Select the brand of your GPU

1. Nvidia
2. AMD/Ryzen
3. CPU 
                       
Choose CPU if GPU is not
capable enough (few VRAM)

0. Go back to more options
------------------------------
```

### NLLB Translation Models

The NLLB translation models are installed automatically with the installer. But for manual installation you must install them through the More Options menu after the rest of the dependencies are installed.

**Steps to install an NLLB model:**

1. Run `python main.py`
2. Go to More Options (option 6)
3. Select Manage AI translation models (option 2)
4. Choose Install new AI translation model (option 2)
5. Pick one of the available models:
   - nllb-200-distilled-600M (fastest, ~650 MB, 1‑2 GB VRAM)
   - nllb-200-distilled-1.3B (balanced, ~1.3 GB, 3‑4 GB VRAM)
   - nllb-200-3.3B (best quality, ~3 GB, 6‑8 GB VRAM)
6. Enter the desired quantization format (recommended: int8)
7. Wait for the model to download, convert, and be stored in models/

After installation, you can switch between installed models from the same menu.
