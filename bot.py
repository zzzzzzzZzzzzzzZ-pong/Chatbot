from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('beetle')
trainer = ListTrainer(chatbot)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"beetle: {chatbot.get_response(query)}")