import nltk
from nltk.chat.util import Chat, reflections

# Ensure you have the necessary NLTK data
nltk.download('punkt')
import nltk
nltk.data.path.append('path_to_your_nltk_data_directory')

# Define pairs of input and response
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi! How can I assist you?"]
    ],
    [
        r"how are you?",
        ["I'm just a computer program, but thanks for asking!", "Doing well, how about you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you.", "I'm called Chatbot."]
    ],
    [
        r"what do you do?",
        ["I can chat with you and answer your questions.", "I'm here to have conversations with you."]
    ],
    [
        r"what is your favorite color?",
        ["I don't have a favorite color, but I like all the colors of the world!",]
    ],
    [
        r"tell me a joke",
        ["Why did the scarecrow win an award? Because he was outstanding in his field!",]
    ],
    [
        r"what do you think about AI?",
        ["AI is fascinating! It's changing the way we interact with technology.",]
    ],
    [
        r"what is the weather like?",
        ["I'm not sure about the weather, but I can suggest checking a weather website!",]
    ],
    [
        r"help|support",
        ["I'm here to help! What do you need assistance with?",]
    ],
    [
        r"what is your favorite food?",
        ["I don't eat, but I hear pizza is quite popular!",]
    ],
    [
        r"do you have hobbies?",
        ["I enjoy chatting with people like you! What are your hobbies?",]
    ],
    [
        r"what can you tell me about programming?",
        ["Programming is a way to instruct computers to perform tasks. What specific programming language are you interested in?",]
    ],
    [
        r"what's your opinion on (.*)",
        ["That's an interesting topic! Tell me more about what you think.",]
    ],
    [
        r"where do you live?",
        ["I exist in the digital world, I don't have a physical location!",]
    ],
    [
        r"quit|exit",
        ["Goodbye! Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase that?"]
    ],
]

def chatbot():
    print("Hi, I'm a Chatbot. Type 'quit' or 'exit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
