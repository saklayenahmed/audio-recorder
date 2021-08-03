import pyaudio
import wave
import datetime
# import time
dateTime= datetime.datetime.now().strftime("%d%m%Y%H%M%S")
# now = time.time()
filename=dateTime+".wav"
chunk = 1024
s_format = pyaudio.paInt16
channels = 2
sample_rate= 48000
record_seconds = int(input("Please tell us in sec: "))

p = pyaudio.PyAudio()

stream = p.open (format=s_format, channels=channels, rate=sample_rate, input=True, output=True, frames_per_buffer=chunk)

frames = []
print("Recording started....")

for i in range(int(sample_rate/chunk * record_seconds)):
    data = stream.read(chunk)
    frames.append(data)

print("Thanks")

stream.stop_stream()
stream.close()
p.terminate()
wv = wave.open(filename,"wb")
wv.setnchannels(channels)
wv.setsampwidth(p.get_sample_size(s_format))
wv.setframerate(sample_rate)
wv.writeframes(b"".join(frames))
wv.close()