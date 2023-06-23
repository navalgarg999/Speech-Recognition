import wave
import numpy as np
import pyaudio

channels = 2

sample_format = pyaudio.paInt32

#record in Frams_per_buffers of 1024 samples
Frams_per_buffer = 1024
fs = 44100 #record at 44100 samples per second

seconds = input('Enter the number of seconds you want to record: ')
seconds = int(seconds)


p = pyaudio.PyAudio()

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate = fs,
                frames_per_buffer=Frams_per_buffer,
                input = True)

frames = []

for i in range(0,int((fs/Frams_per_buffer)*seconds)):
    data = stream.read(Frams_per_buffer)
    frames.append(data)

#stop and close the stream
stream.stop_stream()
stream.close()
#terminate the portaudio interface
p.terminate()

output = "recording.wav"

wf = wave.open(output,'wb')
wf.setnchannels(channels)
wf.setsampwidth((p.get_sample_size(sample_format)))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close

