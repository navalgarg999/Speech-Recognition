import speech_recognition as sr
r = sr.Recognizer()

recording = sr.AudioFile('recording.wav')
with recording as source:
    audio = r.record(source)
r.recognize_google(audio)

recognized_audio = r.recognize_google(audio)
print(recognized_audio)

