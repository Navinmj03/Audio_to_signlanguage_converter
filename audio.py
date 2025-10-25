import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

# Function to convert MP3 to text
def mp3_to_text(mp3_file_path):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file_path)

    # Convert stereo to mono (if needed)
    if audio.channels == 2:
        audio = audio.set_channels(1)

    # Save the mono audio as a temporary WAV file
    wav_file_path = "temp.wav"
    audio.export(wav_file_path, format="wav")

    # Recognize speech using Google Web Speech API
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        # Use Google Web Speech API to convert audio to text
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API; {e}"

# Example usage
mp3_file_path = r"C:\Users\Lenovo\Downloads\mp3-output-ttsfree(dot)com (39).wav"
text_result = mp3_to_text(mp3_file_path)
print("Text Result:", text_result)
