from chatterbot import ChatBot

chatbot = ChatBot('beetle')

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"beetle: {chatbot.get_response(query)}")