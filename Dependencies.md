## Dependencies

This project requires the following main libraries/APPs:

| Library | Purpose | Installation |
|---------|---------|--------------|
| **ONNX Runtime** | ML model inference accelerator by Microsoft. Significantly speeds up the Voice Activity Detection (Silero VAD) used by Whisper. | `pip install onnxruntime` |
| **Whisper** | Speech-to-text transcription model by OpenAI. Converts audio to Spanish text with word-level timestamps. | `pip install openai-whisper` |
| **whisper-timestamped** | Extension of Whisper that provides more accurate word timestamps and integrates Silero VAD for silence detection. | `pip install whisper-timestamped` |
| **CTranslate2** | Fast inference engine for Transformer models. Used to run the NLLB translation model efficiently on CPU. | `pip install ctranslate2` |
| **Transformers** | Hugging Face library for loading and using pre-trained models like NLLB-200. | `pip install transformers` |
| **Silero VAD** | Voice Activity Detection model that identifies speech segments in audio. Helps Whisper avoid transcribing silence. | `pip install silero-vad` |
| **PyTorch** | Deep learning framework used as backend for Whisper, Silero VAD, and Transformers. | `pip install torch torchaudio` |
| **yt-dlp** | YouTube downloader library. Extracts audio from YouTube videos for transcription. | `pip install yt-dlp` |
| **FFmpeg** | Multimedia framework for processing audio and video. Used for audio extraction and burning subtitles into videos. | Install via winget: `winget install ffmpeg` |
