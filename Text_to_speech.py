
#Here i have used google text to speech API for converting text to speech

from gtts import gTTS
import os


def texttospeech():
    try:
        Text= "Hello! Welcome to GitHub!"
        language='en'
        speech=gTTS(Text,lang=language, slow=False)
        speech.save("test.mp3")
        os.system("start test.mp3")

    except UnicodeDecodeError:
        print("Some characters are not supported")

texttospeech()

