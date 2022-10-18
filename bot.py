from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('beetle')
trainer = ListTrainer(chatbot)

trainer.train([
    'Hi',
    'Hello',
    'Assalaamualaikum',
    'Welcome',
    'YOOOOOOOOOOOOOO'
])
trainer.train([
    'this is a bot',
    'message',
    'have u ever thought that the short ppl r actually short'
    'FAST U DUMB GUY'
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"beetle: {chatbot.get_response(query)}")