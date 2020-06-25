import speech_recognition as sr
import pyaudio

p = pyaudio.PyAudio()
r = sr.Recognizer()


def record_audio():
    
    # This is to see wich microhone im using

    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print('Microphones: ', info['index'], info['name'])

    with sr.Microphone() as source:
        print('Say something => ')
        audio = r.listen(source)
        audio_data = r.recognize_google(audio)

        try:
            # for testing purposes, we're just using the default API key

            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

            # instead of `r.recognize_google(audio)`

            print("Google Speech Recognition thinks you said => " + audio_data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
