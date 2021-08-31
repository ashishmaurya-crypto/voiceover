from googletrans import Translator
import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
mic = sr.Microphone()
print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=0)
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("say something")
    audio = r.listen(source)
result = r.recognize_google(audio)
print(result)

Translator = Translator()
k = Translator.Translator(result, 'hindi')
translated = str(k.text)
print(translated)


engine = pyttsx3.init()
engine.say(translated)
engine.runAndWait()
    
