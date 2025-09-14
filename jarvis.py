import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib
import requests
from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv() 

newsapi = os.getenv("NEWSAPI_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
     try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": command}
            ] 
        )
        return completion.choices[0].message.content 
     except Exception as e:
          print("Error:OpenAi is not responding..")

     
def processCommand (c):
     print(c)
     if "open google" in c.lower():
          webbrowser.open("https://google.com")
          
     elif "open youtube" in c.lower():
          webbrowser.open("https://youtube.com")
          
     elif "open linkedin" in c.lower():
          webbrowser.open("https://www.linkedin.com")
          
     elif c.lower().startswith("play"):
          song = c.lower().split(" ")[1]
          link = musicLib.music[song]
          webbrowser.open(link)

     elif "news" in c.lower():
          r =requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=6e0bdef2b08640eaa14ab56027c594f1")
          if r.status_code == 200:
               data = r.json()
               articles =data.get("articles",[])

               for article in articles:
                    speak(article['title'])
     else:
          output = aiProcess(c)
          print(f"Ai Response:{output}")
          speak(output)
                    
if __name__ == "__main__":
    speak("Initializing  Jarvis.....")
    
    while True:
            r= sr.Recognizer()
            print("Recognizing.....")

            try:
                 
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source,timeout=2)                   
                word = r.recognize_google(audio)
                print(word)

                if "jarvis" in word.lower():
                    speak("Yeah")
                    with sr.Microphone() as source:
                        print("Jarvis active...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)
            
            except Exception as e:
                print("Error;")

