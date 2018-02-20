
from chatterbot import ChatBot
import sys

#get the passed path of the training file
training_file_path = sys.argv[1]
#get the string argument client_chat from post
send_chat_to_bot = sys.argv[2]
# Create a new instance of a ChatBot
bot = ChatBot(
    'Default Response Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)
readTrainingData = open(training_file_path,'r').readlines()
# Train the chat bot with the training file
bot.train(readTrainingData)

# Get a response for some unexpected input
response = bot.get_response(send_chat_to_bot)
print(response)