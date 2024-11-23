import random 

# RESPONSES OF CHATBOT
responses = {
    "hi" : ["Hello!🙌", "Hi there!👀", "Hey! How can I help you?😎"], 
    "hii" : ["Hello!🙌", "Hi there!👀", "Hey! How can I help you?😎"], 
    "hello": ["Hello!🙌", "Hi there!👀", "Hey! How can I help you?😎"],
    "hey": ["Hello!🙌", "Hi there!👀", "Hey! How can I help you?😎"],
    "hiii": ["Hello!🙌", "Hi there!👀", "Hey! How can I help you?😎"],
    "hellooo": ["Hello!🙌", "Hi there!👀", "Hey! How can I help you?😎"],
    "how are you": ["I'm doing well, thank you!😋", "I am good, how are you?😀", "I'm just a bot, but I'm doing great!😇"],
    "how are you doing": ["I'm doing well, thank you!😋","I am good, how are you?😀", "I'm just a bot, but I'm doing great!😇"],
    "how are you doing today": ["I'm doing well, thank you!😋","I am good, how are you?😀", "I'm just a bot, but I'm doing great!😇"],
    "hry": ["I'm doing well, thank you!😋","I am good, how are you?😀", "I'm just a bot, but I'm doing great!😇"],
    "hru": ["I'm doing well, thank you!😋","I am good, how are you?😀", "I'm just a bot, but I'm doing great!😇"],
    "bye": ["Goodbye!😁", "See you later!😏", "Have a great day!🤗"],
    "goodbye": ["Goodbye!😁", "See you later!😏", "Have a great day!🤗"],
    "see you later": ["Goodbye!😁", "See you later!😏", "Have a great day!🤗"],
    "what is your name": ["I'm a chatbot, I don't have a name. You can call me whatever you like!😉", "I'm your friendly bot, no name needed!😎"],
    "name": ["I'm a chatbot, I don't have a name. You can call me whatever you like!😉", "I'm your friendly bot, no name needed!😎"],
    "who are you": ["I'm a chatbot, I don't have a name. You can call me whatever you like!😉", "I'm your friendly bot, no name needed!😎"],
    "what are you": ["I'm a chatbot, I don't have a name. You can call me whatever you like!😉", "I'm your friendly bot, no name needed!😎"],
    "ok": ["Okay!😊", "Great!😃", "Alright!😄"],
    "okay": ["Okay!😊", "Great!😃", "Alright!😄"],
    "great": ["Okay!😊", "Great!😃", "Alright!😄"],
    "alright": ["Okay!😊", "Great!😃", "Alright!😄"],
    "i am good": ["Good to know!😁", "Nicee😍"],
    "i am fine": ["Good to know!😁", "Nicee😍"],
    "i am great": ["Good to know!😁", "Nicee😍"],
    "i am ok": ["Good to know!😁", "Nicee😍"],
    "i am okay": ["Good to know!😁", "Nicee😍"],
    "nothing": ["Okay!😊", "Great!😃", "Alright!😄"],
    "i feel sad": ["I'm sorry to hear that.😞", "I hope you feel better soon.😔", "Is there anything I can do to help?😥"],
    "i feel happy": ["That's great to hear!😊", "I'm glad you're happy!😁", "That's wonderful!😃"],
    "i feel excited": ["That's great!😊", "I'm glad you're excited!😃", "That's wonderful!😃"],
    "i feel angry": ["I'm sorry to hear that.😞", "I hope you feel better soon.😔", "Is there anything I can do to help?😥"],
    "i feel tired": ["I'm sorry to hear that.😞", "I hope you feel better soon.😔", "Is there anything I can do to help?😥"],
    "i feel hungry": ["I'm sorry to hear that.😞", "I hope you feel better soon.😔", "Is there anything I can do to help?😥"],
    "i feel thirsty": ["I'm sorry to hear that.😞", "I hope you feel better soon.😔", "Is there anything I can do to help?😥"],
    "thank you": ["You're welcome!😊", "No problem!😃", "Anytime!😄"],
    "thanks": ["You're welcome!😊", "No problem!😃", "Anytime!😄"],
    "sorry":["Don't worry!"],
    "what is the date": ["You’re literally using a device that shows the date. Nice try though. 😅"],
    "what is the day": ["Oh, it’s that day... you know, the one where you finally get stuff done! 😅"],
    "why": ["I have very limited access😶", "sorry for the inconvenience😢"],
    "its ok": ["Okay!😊", "Great!😃", "Alright!😄"],
    "it is ok": ["Okay!😊", "Great!😃", "Alright!😄"],
    "what is my name": ["I'm sorry, I don't have access to your name.😔", "I'm afraid I can't tell you your name.😞", "I'm not sure what your name is.😕"],
    "what are you doing": ["I am at your service😊", "I am here to help😁", "I am ready to assist you😃"],
    "what is your purpose": ["I am here to assist you😁", "I am here to help😁"], 
    "what is your favorite book": ["I don't have a favorite book, I'm just a bot!😊", "I don't have a favorite book, I'm just a bot!😊", "I don't have a favorite book, I'm just a bot!😊"],
    "what is your favorite color": ["I don't have a favorite color, I'm just a bot!😊", "I don't have a favorite color, I'm just a bot!😊", "I don't have a favorite color, I'm just a bot!😊"],
    "what is your favorite food": ["I don't have a favorite food, I'm just a bot!😊", "I don't have a favorite food, I'm just a bot!😊", "I don't have a favorite food, I'm just a bot!😊"],
    "what is your favorite movie": ["I don't have a favorite movie, I'm just a bot!😊", "I don't have a favorite movie, I'm just a bot!😊", "I don't have a favorite movie, I'm just a bot!😊"],
    "salam": ["Salam!🎀", "WalikumSalaam✨"],
    "assalamualaikum":["Salam!🎀", "WalikumSalaam✨"],
    "assalamu alaikum": ["Salam!🎀", "WalikumSalaam✨"],
    "assalamualaikum wa alaikum": ["Salam!🎀", "WalikumSalaam✨"],
    "tell me the date":["You’re literally using a device that shows the date. Nice try though. 😅"],
    "tell me the time":["Time is an illusion, friend. But if you insist... it’s now o'clock."],
    "tell me the day":["Oh, it’s that day... you know, the one where you finally get stuff done! 😅"],
    "oh":["Oh. Just 'oh'? I expected a bit more drama. 😅"],
    "ohh":["Oh. Just 'oh'? I expected a bit more drama. 😅"],
    "ohhh":["Oh. Just 'oh'? I expected a bit more drama. 😅"],
    "nice":["Nice? I’ll take that as a compliment! 😁"],
    "nice":["Good? I’ll take that as a compliment! 😁"],
    "whats the date":["You’re literally using a device that shows the date. Nice try though. 😅"],
    "whats the time":["Time is an illusion, friend. But if you insist... it’s now o'clock."],
    "whats the day":["Oh, it’s that day... you know, the one where you finally get stuff done! 😅"],
    "what's the date":["You’re literally using a device that shows the date. Nice try though. 😅"],
    "what's the time":["Time is an illusion, friend. But if you insist... it’s now o'clock."],
    "what's the day":["Oh, it’s that day... you know, the one where you finally get stuff done! 😅"],
    "what is the weather": ["I can tell you it’s definitely not raining cats and dogs. I checked. 🐱🐶"],
    "what is the temperature": ["It’s cool, but I’m way cooler. ❄️😏"],
    "haha": ["Haha!😂", "Haha!😂", "Haha!😂"],
    "hahaa": ["Haha!😂", "Haha!😂", "Haha!😂"],
    "hahaaa": ["Haha!😂", "Haha!😂", "Haha!😂"],
    "hahaaaa": ["Haha!😂", "Haha!😂", "Haha!😂"],
    "hahaaaaa": ["Haha!😂", "Haha!😂", "Haha!😂"],
    "good one": ["AW TY"],
    "yes": ["Okay!😊", "Great!😃", "Alright!😄"],
    "no": ["Okay!😊", "Great!😃", "Alright!😄"],
    "leave it": ["AS YOU SAY"],
    "leave": ["Okay!😊", "Great!😃", "Alright!😄"],
    "aw":["Aww, you just made me smile! 😊"],
    "what is my name":["If only I had a memory... But for now, you’re my mysterious friend! 😄"],
    "what month is right now" : ["Sorry, I dont have access to that info"],
    "default": ["Sorry, I didn't understand that.😅", "Can you rephrase that?🙃", "I'm not sure how to respond to that.😔"]
    
}


def getResponse(input): 
   
    input = input.lower()
    
    if input in responses:
        return random.choice(responses[input])
    else:
        return random.choice(responses["default"])


def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot, Type exit to end the conversation.")
    
    while True:
        
        Input = input("You: ")
        
        
        if Input.lower() == "exit":
           
            break
        
        response = getResponse(Input)
        
        
        print("ChatBot:", response)
        


chatbot()

