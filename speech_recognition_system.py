import speech_recognition as sr

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    return recognizer.recognize_google(audio_data)

if __name__ == "__main__":
    audio_path = "sample.wav"
    print("Transcription:\n", transcribe_audio(audio_path))
