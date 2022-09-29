#thư viện

from datetime import datetime
from datetime import date
from matplotlib import cm
from time import sleep
import random
from rich.progress import track
import webbrowser
import datetime
import pyttsx3
import speech_recognition
from pyowm import OWM
import pyowm
from pyowm.utils import config
from pyowm.utils import timestamps
import pyautogui
import subprocess
import os

#tạo

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
robot_mouth = pyttsx3.init()
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[17].id)
robot_mouth.say("Hello World")
robot_mouth.runAndWait()
#python terminal colors| thông tin

#print("\033[36m-=-=-= \033[33mTRỢ LÝ ẢO \033[37mKHÁNH\033[35m(AI) \033[36m=-=-=-")
#print("\033[34mTrợ lý ảo KhánhAI \033[33mcode by \033[32mBảo Mondy")
#print("\033[33mRunning Troliaov2")
#print("\033[31mChạy trợ lý ảo...")
#for i in track(range(10), description="\033[31mĐang chạy......"):
#    print(f"\033[33mxong \033[32m{i}\033[33m%")
#   sleep(0.5)
while True:
    with speech_recognition.Microphone() as mic:
        print("\033[32mBảoAI: \033[37mtoi dang nghe...")
        audio = robot_ear.listen(mic)

    print("\033[32mBảoAI: \033[37mđang suy nghĩ...")

#trả lời câu hỏi


    try:
        you = robot_ear.recognize_google(audio)
    except:

        you = ""

    print("\033[33myou: \033[39m" + you)

    if you == "":
        robot_brain = "I can't hear you, try again"
    
    elif you == "hey robot":
        robot_brain = "what's up?"
    elif you == "hello":
        robot_brain = "hello Bao"
    
    elif you == "today":
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    
    elif you == "now":
        now = datetime.datetime.now()
        robot_brain = now.strftime("%I:%M:%p")
   
    elif you == "i want to have sex with you":
        robot_brain = "who the fuck are you"
   
    elif you == "how do you think about me":
        robot_brain = "Bao is very handsome and smart"
   
    elif you == "how are you":
         robot_brain = "I'm fine thank you and you ?"
   
    elif you == "who are you":
        robot_brain = "I'm Bao's lover"
    
    elif you == "how old are you":
         robot_brain = "I'm 1 year old"
   
    elif "YouTube" in you:
        webbrowser.open('https://www.youtube.com')
        robot_brain = "open youtube"
    
    elif "Google" in you:
        webbrowser.open('https://www.google.com')
        robot_brain = "open google"
    
    elif "Spotify" in you:
        webbrowser.open('https://www.spotify.com')
        robot_brain = "open spotify"
    
    elif "Facebook" in you:
        webbrowser.open('https://www.facebook.com')
        robot_brain = "open facebook"
    
    elif "messenger" in you:
        webbrowser.open('https://www.messenger.com')
        robot_brain = "open messenger"
    
    elif "weather" in you:
        owm = OWM('023f8075107f72dd81cf7c25cdbc6e30')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place('Hue,VN')
        w = observation.weather

        w.detailed_status         
        w.wind()                 
        w.humidity               
        w.temperature('celsius')  
        w.rain                    
        w.heat_index              
        w.clouds       
        print("\u001b[33mToday:\u001b[0m")
        print(w.detailed_status)
        print("\u001b[33mWind:\u001b[0m")
        print(w.wind())
        print("\u001b[33mhumidity\u001b[35m(%)\u001b[33m:\u001b[0m")
        print(w.humidity)
        print("\u001b[33mtemperature\u001b[35m(ºC)\u001b[33m:\u001b[0m")
        print(w.temperature('celsius'))
        print("\u001b[33mRain:\u001b[0m")
        print(w.rain)
        print("\u001b[33mheat index:\u001b[0m")
        print(w.heat_index)
        print("\u001b[33mcloud\u001b[35m(%)\u001b[33m:\u001b[0m")
        print(w.clouds)
        robot_brain = "weather in Hue"
    elif "screenshot" in you:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'ảnh.png') 
        robot_brain = "the screen has been captured"
    elif "camera" in you:
        os.system("open Photo\ Booth.app")


    #kết thúc
    
    elif you == "goodbye":
        robot_brain = "bye Bao"
        print("\033[32mKhanhAI: \033[39m" + robot_brain)
        robot_mouth = pyttsx3.init()
        robot_mouth.setProperty("rate", 150)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    
    #các trường hợp còn lại

    else:
        robot_brain = "I can't answer your question"

    print("\033[32mBaoAI: \033[39m" + robot_brain)
   
    #giọng nói

    robot_mouth = pyttsx3.init()
    voices = robot_mouth.getProperty('voices')
    robot_mouth.setProperty('voice', voices[10].id)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()