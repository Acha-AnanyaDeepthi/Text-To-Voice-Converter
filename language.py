from gtts import gTTS
import os
import platform

# Optional: Common languages
language_options = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'hi': 'Hindi',
    'ta': 'Tamil',
    'zh': 'Chinese',
    'ja': 'Japanese',
    'ru': 'Russian'
}

print("Available languages:")
for code, lang in language_options.items():
    print(f"{code} - {lang}")

# Get user input
text = input("\nEnter your text: ")
language = input("Enter language code (e.g., 'en' for English): ").strip().lower()

# Check if the entered language is valid
if language not in language_options:
    print("Invalid or unsupported language code. Defaulting to English (en).")
    language = 'en'

# Convert text to speech
tts = gTTS(text=text, lang=language, slow=False)
tts.save("audio.mp3")

# Play the audio
if platform.system() == "Windows":
    os.system("start audio.mp3")
elif platform.system() == "Darwin":
    os.system("afplay audio.mp3")
else:
    os.system("mpg123 audio.mp3")
