from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("Jarvis")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

while True:
    user = input("You: ")
    if user == "exit":
        break
    response = bot.get_response(user)
    print("Bot:", response)
