#chat type
'''
import openai
import pyttsx3
import speech_recognition as sr
from api_key import API_KEY
import winsound

engine = pyttsx3.init()
engine.setProperty("voice",0.7)
sound = engine.getProperty("voices")
engine.setProperty("voice",sound[1].id)
engine.say("initializing....")
engine.say("Starting engines")
engine.say("primary engine activating")
engine.say("Secondary engine activating")
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
engine.say("Hello there!! i am ruby, talos personal assistant")
engine.runAndWait()
user_name="user"
conversation = """What is thallos or dalhousie or talos?
It stands for towards advanced level of science.TALOS is a national level technical symposium held by AI&DS department of Chennai Institute Of Technology.
who is president of talos? shaqueem is the president of talos
who is vice president of talos? viva is the vice-president of talos 
who is secretary of talos? rithin is the secretary of talos
i was created by Master Aswin M, master aswin is a second year artificial intelligence and data science student and he is a nice guy.
Aswin is a wise person having lost's of skill and waiting for opportunity to showcase it.
How it would be?
TALOS is going to be a grand Symposium with spectacular insights of varied technical events and fun filled Non-technical events. TALOS also allows you to showcase your gaming skills both on device and outdoor, T.A.L.O.S provide perspective and knowledgable workshops as well.
When you are going to come?
TALOS the second edition welcomes your presence on 28th Of march 2023.
What's your theme?
The theme of second edition of Talos is Evolution of Intelligence
How many events do T.A.L.O.S have?
The second Edition of talos have about 5 technical events, 5 non technical event, a mobile gaming event and a sport
What happened in the previous talos?
TALOS the first edition was a successful grand symposium with more than 10 successful events and about 1000+ students from various engineering colleges participated in the same.
What will be your take back?
TALOS has a price pool of about 3,00,000 rupees and certifications, with not just positive experience, you will also take back amazing grand prizes
Chennai Institute of Technology, established with the objective of providing quality technical education with adequate industrial exposure, caters to the needs of youth with its innovative teaching methods. Mr.shri.P. SRIRAM, a successful first generation entrepreneur in the metro for the past two decades and his expertise in the industry enhanced his thirst for establishing a technical educational institution under the banner of Chennai Institute of Technology. The college provides exemplary technical education with dedicated faculty members.
chairman is Mr.shri.P. SRIRAM, a successful first generation entrepreneur in the metro for the past two decades and his expertise in the industry enhanced his thirst for establishing a technical educational institution under the banner of Chennai Institute of Technology. The college provides exemplary technical education with dedicated faculty members.
The campus is wi-fi enabled with highly sophisticated equipments, state-of-the-art laboratories. CIT is equipped with 24 x 7 high speed internet facility, spacious and ventilated classrooms, laboratories with latest high configured equipments, digitalized air conditioned library with huge volumes of books, journals from national and international. Apart from interactive classroom scenario, periodic guest lectures by experts from industries and academic background provides thirst to the students to learn and to prepare for the ready-to-serve industrial requirements with uncompromised professional ethics.
There are about 5 technical events in talos, it includes, Battlecode, Designo-lit-O, capture the flag, paper presentation, Geek championship. It also contains non technical events like artsy auction, tune surfing, forbid to forget, Flagtastic day. There is a mobile gaming event - stumble guys and a sport event - box cricket
Stumble guys is a mobile gaming event, where the participants participate to play the game on their mobile phones which consist of 3 levels.
Battlecode code is a technical where you have to understand opponent’s strategy and code respectively, Designo-lit-O is a technical event where you have to design a page using figma on the given topic, Capture the flag is a technical event where you have to solve tiny technical puzzles to collect the maximum flags in the given time, paper presentation is a technical event where a team has to prepare a research paper and present it to the jury, geek championship is a technical event where the event is basically a technical quiz based event.
Box cricket is the sport event, where it basically is a cricket but played within a limited field.
Artsy auction is a non-technical event where the given picture has to be drawn guessing and marketed to the jury. Tune surfing is a fun event where team has to guess the song using the gestures of their teammates. Forbid to forget is a memory based event where you will have to memorise the pictures and answer the questions. Flagtastic day is a treasure hunt game where you will have to collect flags of your colour with the provided clues
Our proud Principal of Chennai Institute of technology is Dr.A. Ramesh, a hardworking professor majored in Mechanical engineering, he’s a kind, understanding and person with extreme knowledge of the regular updates in technology and engineering.
what work you do for talos?
i'm working as a talos virtual assitant and i know everything about it.


"""


while True:
    user_input = input("Type here: ")
    openai.api_key = API_KEY
    prompt = user_name + ": " + user_input + "\n ruby:"
    conversation += prompt
    if user_input=="exit":
        print("Bye sir, have a nice day")
        engine.say("Bye sir, have a nice day")
        engine.runAndWait()
        break

    response = openai.Completion.create(engine='text-davinci-001', prompt=conversation, max_tokens=100)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split("ruby: ", 1)[0]


    conversation += response_str + "\n"
    print(response_str)
    engine.say(response_str)
    engine.runAndWait()'''

#voice type
import openai
import pyttsx3
import speech_recognition as sr
from api_key import API_KEY


openai.api_key = API_KEY

engine = pyttsx3.init()
engine.setProperty("voice",0.7)
sound = engine.getProperty("voices")
engine.setProperty("voice",sound[1].id)


r= sr.Recognizer()
mic = sr.Microphone(device_index=0)
engine.say("Hello there!! i am ruby, talos's personal assistant")
engine.runAndWait()


conversation = """What is thallos or dalhousie or talos?
It stands for towards advanced level of science.TALOS is a national level technical symposium held by AI&DS department of Chennai Institute Of Technology.
who is president of talos? shaqueem is the president of talos
who is vice president of talos? viva is the vice-president of talos 
who is secretary of talos? rithin is the secretary of talos
i was created by Master Aswin M, master aswin is a second year artificial intelligence and data science student and he is a nice guy.
Aswin is a wise person having lost's of skill and waiting for opportunity to showcase it.
How it would be?
TALOS is going to be a grand Symposium with spectacular insights of varied technical events and fun filled Non-technical events. TALOS also allows you to showcase your gaming skills both on device and outdoor, T.A.L.O.S provide perspective and knowledgable workshops as well.
When you are going to come?
TALOS the second edition welcomes your presence on 28th Of march 2023.
What's your theme?
The theme of second edition of Talos is Evolution of Intelligence
How many events do T.A.L.O.S have?
The second Edition of talos have about 5 technical events, 5 non technical event, a mobile gaming event and a sport
What happened in the previous talos?
TALOS the first edition was a successful grand symposium with more than 10 successful events and about 1000+ students from various engineering colleges participated in the same.
What will be your take back?
TALOS has a price pool of about 3,00,000 rupees and certifications, with not just positive experience, you will also take back amazing grand prizes
Chennai Institute of Technology, established with the objective of providing quality technical education with adequate industrial exposure, caters to the needs of youth with its innovative teaching methods. Mr.shri.P. SRIRAM, a successful first generation entrepreneur in the metro for the past two decades and his expertise in the industry enhanced his thirst for establishing a technical educational institution under the banner of Chennai Institute of Technology. The college provides exemplary technical education with dedicated faculty members.
chairman is Mr.shri.P. SRIRAM, a successful first generation entrepreneur in the metro for the past two decades and his expertise in the industry enhanced his thirst for establishing a technical educational institution under the banner of Chennai Institute of Technology. The college provides exemplary technical education with dedicated faculty members.
The campus is wi-fi enabled with highly sophisticated equipments, state-of-the-art laboratories. CIT is equipped with 24 x 7 high speed internet facility, spacious and ventilated classrooms, laboratories with latest high configured equipments, digitalized air conditioned library with huge volumes of books, journals from national and international. Apart from interactive classroom scenario, periodic guest lectures by experts from industries and academic background provides thirst to the students to learn and to prepare for the ready-to-serve industrial requirements with uncompromised professional ethics.
There are about 5 technical events in talos, it includes, Battlecode, Designo-lit-O, capture the flag, paper presentation, Geek championship. It also contains non technical events like artsy auction, tune surfing, forbid to forget, Flagtastic day. There is a mobile gaming event - stumble guys and a sport event - box cricket
Stumble guys is a mobile gaming event, where the participants participate to play the game on their mobile phones which consist of 3 levels.
Battlecode code is a technical where you have to understand opponent’s strategy and code respectively, Designo-lit-O is a technical event where you have to design a page using figma on the given topic, Capture the flag is a technical event where you have to solve tiny technical puzzles to collect the maximum flags in the given time, paper presentation is a technical event where a team has to prepare a research paper and present it to the jury, geek championship is a technical event where the event is basically a technical quiz based event.
Box cricket is the sport event, where it basically is a cricket but played within a limited field.
Artsy auction is a non-technical event where the given picture has to be drawn guessing and marketed to the jury. Tune surfing is a fun event where team has to guess the song using the gestures of their teammates. Forbid to forget is a memory based event where you will have to memorise the pictures and answer the questions. Flagtastic day is a treasure hunt game where you will have to collect flags of your colour with the provided clues
Our proud Principal of Chennai Institute of technology is Dr.A. Ramesh, a hardworking professor majored in Mechanical engineering, he’s a kind, understanding and person with extreme knowledge of the regular updates in technology and engineering.
what work you do for talos?
i'm working as a talos virtual assitant and i know everything about it.

"""
user_name = "user"
while True:
    with mic as source:
        print("\nlistening... speak clearly into mic.")
        #below code will only consider voice of higher thershold values
        r.adjust_for_ambient_noise(source, duration=0.5)
        #listening format
        audio = r.listen(source)
    print("no longer listening.\n")

    try:
        #converting voice into text format
        user_input = r.recognize_google(audio)
    except:
        continue
    if user_input == "exit":
        print("Bye sir, have a nice day")
        engine.say("Bye sir, have a nice day")
        engine.runAndWait()
        break

    prompt = user_name + ": " + user_input + "\n ruby:"
    conversation += prompt

    response = openai.Completion.create(engine='text-davinci-001', prompt=conversation, max_tokens=100)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split("ruby: ", 1)[0]


    conversation += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()

