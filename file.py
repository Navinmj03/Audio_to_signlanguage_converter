from gtts import gTTS
import os
from googletrans import Translator
import speech_recognition as sr

# Speech Recognition
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something in Hindi:") 
    audio = recognizer.listen(source)

# Recognize and translate
try:
    hindi_text = recognizer.recognize_google(audio, language="hi-IN")
    print("You said (Hindi):", hindi_text)

    # Translation using googletrans
    translator = Translator()
    translation = translator.translate(hindi_text, dest="en")
    english_translation = translation.text
    print("Translated to English:", english_translation)

    # Text-to-Speech (English)
    tts_english = gTTS(english_translation, lang='en')
    tts_english.save("output_english.mp3")

    # Play the generated English audio file
    os.system("start output_english.mp3")

except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")