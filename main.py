import speech_recognition as sr
from time import ctime
import webbrowser
import pyaudio

p = pyaudio.PyAudio()
r = sr.Recognizer()


def record_audio(ask=False):

    # This is to see wich microhone im using

    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        # print('Microphones: ', info['index'], info['name'])

    with sr.Microphone() as source:
        if ask:
            print(ask)

        audio = r.listen(source)
        voice_data = ''

        try:
            # for testing purposes, we're just using the default API key

            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

            # instead of `r.recognize_google(audio)`

            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
        return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Alexis')
    if 'What time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for? ')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search)


print('How can I help you ? ')
voice_data = record_audio()
respond(voice_data)
