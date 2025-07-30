# SPEECH-RECOGNITION-SYSTEM

 *COMPANY*: CODTECH IT SOLUTIONS

*NAME*: AKULA GOWRI SHANKAR

*INTERN ID*: CT04DH833

*DOMAIN*: AI(ARTIFICIAL INTELLIGENCE)

*DURATION*:4 WEEKS

*MENTOR*: NEELA SANTOSH

## DESCRIPTION

This script uses the speech_recognition library in Python, a popular choice for speech-to-text tasks thanks to its easy-to-use interface and integration with powerful backend engines like Google Speech Recognition.

1. Library Initialization
The code starts by importing the speech_recognition module, abbreviated as sr. This module serves as a wrapper around various speech recognition APIs, such as Google, IBM, Sphinx, and others. Here, we use the Google Web Speech API because it’s simple, effective, and doesn’t require authentication for short clips.

2. Defining the Transcription Logic
The function transcribe_audio(audio_file) is where all the core processing happens:

Recognizer Instantiation: We create an instance of the Recognizer class, which provides the interface for recording and transcribing audio.

Audio File Handling: Using Python’s with statement, we open the audio file (.wav format is ideal and supported by the library). The recognizer reads the contents of the audio clip into memory using record(source).

Transcription: The recognize_google() method sends the audio data to Google's speech recognition API. Google processes the audio and returns a string of recognized text, which is the function's return value.

3. Script Execution Block
When the script is run, it:

Loads an audio file named sample.wav.

Passes this file into the transcribe_audio() function.

Prints the transcribed text on the console.

You can replace "sample.wav" with any other file name, as long as it's a valid .wav audio clip with clear speech. Note that background noise or multiple overlapping speakers can degrade recognition quality.

Why This Matters
This system is simple by design, but it encapsulates what most commercial voice input systems do under the hood. The benefits are substantial:

Accessibility: Helps users with disabilities interact with digital platforms using voice.

Productivity: Speeds up tasks like note-taking, transcription, and command execution.

Integration-Ready: This script can be embedded into larger systems—chatbots, meeting assistants, or smart devices—thanks to its modular structure.

Moreover, since this implementation uses a pre-trained model via Google’s API, it doesn't require you to build or train any models yourself. This makes it especially helpful for rapid prototyping or building lightweight applications.

For more advanced systems, you could replace recognize_google() with a local Wav2Vec2 model from Hugging Face Transformers if you need offline capabilities or have privacy concerns about sending audio to external servers.

## OUTPUT

Transcription: 2 + 7 is less than 10
