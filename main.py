import speech_recognition as sr
from time import ctime
from gtts import gTTS
import webbrowser
import playsound
import pyaudio
import random
import time
import os

p = pyaudio.PyAudio()
r = sr.Recognizer()


def record_audio(ask=False):

    # This is to see wich microhone my computer have

    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        # print('Microphones: ', info['index'], info['name'])

    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)

        audio = r.listen(source)
        voice_data = ''

        try:
            # for testing purposes, we're just using the default API key

            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

            # instead of `r.recognize_google(audio)`

            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexis_speak(
                "Sorry, could you repeat, please?")
        except sr.RequestError as e:
            alexis_speak(
                "Sorry, I have some problems to solve now, try again later; {0}".format(e))
        return voice_data


def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is Camila, nice too meet you!')
    if 'nice to meet you too' in voice_data:
        alexis_speak('thanks, so, how can I help you? ')
    if 'What time is it' in voice_data:
        alexis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for? ')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location ? ')
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
alexis_speak('How can I help you ? ')
while(1):
    voice_data = record_audio()
    respond(voice_data)
