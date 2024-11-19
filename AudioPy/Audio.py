import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

print(device)
# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

print("Done")

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
#wav = tts.tts(text="Hello world!", speaker_wav="Param-audio.wav", language="hi")
# Text to speech to a file
tts.tts_to_file(text="प्राचीन भारत में, अयोध्या नगरी में राजा दशरथ और रानी कौशल्या का पुत्र राम था। राम एक अद्भुत और धर्मनिष्ठ राजा था, जिसे उसके न्याय और साहस के लिए जाना जाता था।", speaker_wav="Param-audio.wav", language="hi", file_path="output.wav")