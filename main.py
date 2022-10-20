# In-Built Jarvis for Iron Man Helmet MK3 Replica

import speech_recognition as sr
import festival
import datetime

festival.initialize(1, 210000)

now = datetime.datetime.now()

while True:
    with sr.Microphone() as source:

        r = sr.Recognizer()
        hot_word='Jarvis'
        audio=r.listen(source)
        inpt = r.recognize_google(audio)
        if hot_word in inpt:

            if "hi" in inpt:
                result = "Greetings, Sir."

            if "hello" in inpt:
                result = "Hello, Sir."

            if "hey" in inpt:
                result = "Hello, hows it going?"

            if "how are you" in inpt:
                result = "It's going well, Sir. Yourself?"

            if "how's it going" in inpt:
                result = "Well, sir. What about yourself?"

            if "bye" in inpt:
                result = "Shutting down, Sir. See you next time."

            if "m well" in inpt:
                result = "I am glad to hear that, sir."
            
            if "m good" in inpt:
                result = "That's great, Sir. "

            if "doing bad" in inpt:
                result = "I am sorry to hear this news, sir."
            
            if "see you" in inpt:
                result = "good luck"

            if "not well" in inpt: 
                result = "My apologies, sir."

            if "goodbye" in inpt:
                result = "Goobye, Sir. "

            if "I don't know" in inpt:
                result = "Copy that, sir."
            if "no" in inpt:
                result = "Alright."
            
            if "thank you" in inpt:
                result = "Anytime, sir."
            
            if "you there" in inpt:
                result = "Of course, sir. How may I be of assitance?"

            if "you up" in inpt:
                "For you sir, always."

            if "nevermind" in inpt:
                result = "Understood, Sir."

            if "power down" in inpt:
                result = "Powering down all systems. Until next time, Sir. "

            if "Yes" in inpt:
                result = "On it."

            if "time" in inpt:
                result = ("The current time is " + now.strftime("%H") + " hours and " + now.strftime("%M") + " minutes.")

            if "date"  in inpt:
                result = ("The current month is " + now.strftime("%m") + " , and the year is " + now.strftime("%Y") + ".")
            
            if "yes" in inpt:
                result = "Of course."


            print('You: ' + r.recognize_google(audio))
            print('Jarvis: ' + result)
            festival.say(result)
