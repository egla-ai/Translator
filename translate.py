import speech_recognition as sr  # SpeechRecognition library
from pydub import AudioSegment  # Library for audio file conversion
import os  # For path manipulation

def convert_mp3_to_wav(mp3_file_path):
    """Convert MP3 file to WAV format."""
    wav_file_path = mp3_file_path.rsplit('.', 1)[0] + '.wav'  # Replace .mp3 with .wav
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format='wav')
    return wav_file_path

def transcribe_audio(mp3_file_path):
    """Transcribe audio from the given file using Google Speech Recognition."""
    r = sr.Recognizer()  # Initialize the Recognizer

    with sr.AudioFile("Kothbiro.mp3") as source:  
        print("Processing audio...")
        audio = r.record(source)  # Use record() to read the entire file

        try:
            # Recognize the speech using Google's speech recognition
            speech_text = r.recognize_google(audio)
            print("Transcribed Text: ")
            print(speech_text)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    # Provide the path to your MP3 audio file here
    mp3_file_path = 'Kothbiro.mp3'  # Update this with your file path

    # Check if the provided file is an MP3
    if mp3_file_path.lower().endswith('.mp3'):
        # Convert MP3 to WAV
        wav_file_path = convert_mp3_to_wav(mp3_file_path)
        print(f"Converted '{mp3_file_path}' to '{wav_file_path}'.")

        # Transcribe the WAV audio file
        transcribe_audio(wav_file_path)
        
        # Optionally, remove the WAV file after transcription if you don't need it
        os.remove(wav_file_path)
    else:
        print("Please provide a valid MP3 file.")
