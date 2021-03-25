import pyaudio
import wave
from time import sleep
import speech_recognition as sr
import subprocess
from commands import Commander
import subprocess
import os
from get_answer import Fetcher


#def say(text):
#	subprocess.call('say ' + text, shell=True)

def play_audio(filename):
	chunk = 1024
	wf = wave.open(filename,'rb')
	pa = pyaudio.PyAudio()

	stream = pa.open(
		format=pa.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True
	)

	data_stream = wf.readframes(chunk)

	while data_stream:
		stream.write(data_stream)
		data_stream = wf.readframes(chunk)

	stream.close()
	pa.terminate()

def respond(response):
    print(response)
    subprocess.call("say " + response, shell=True)	

def discover(text):
    if "what" in text and "name" in text:
        if "my" in text:
            respond("You have not told me your name yet")
        else:
                respond("My name is companion , How are you?")
    elif  "launch" in text   or "open" in text:
        app = text.split(" ", 1)[-1]
        if app == "browser":
            respond("Opening browser")
            subprocess.call("google-chrome")
        elif app == "editor":
            respond("Opening text-editor")
            subprocess.call("subl")
        else:
            respond("I dont think I am allowed to do that")
    else:
        f = Fetcher("https://www.google.com/search?q=" + text)
        ans = f.lookup()
        respond(ans)	

#play_audio("./audio/done.wav")

r = sr.Recognizer();
run = True

def initSpeech():
	print("Listening...")
	play_audio("./audio/wet.wav")

	with sr.Microphone() as source:
		print("Say something")
		audio = r.listen(source)

	play_audio("./audio/done.wav")
	command = ""

	try:
		command = r.recognize_google(audio)
	except Exception as e:
		print("Couldn't really understand maybe because of the :", e)

	print("Your command:")
	print(command)
	if command in ["quit", "exit", "bye", "goodbye"]:
		global run
		run = False

	discover(command)	
	#say("You said " + command)


while run == True:
	initSpeech()
	sleep(10)				
