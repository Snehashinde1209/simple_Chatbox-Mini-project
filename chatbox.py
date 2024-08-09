reply = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! How are you today?",
    "how are you": "I'm just a bot, but I'm doing well! How about you?",
    "bye": "Goodbye! Have a nice day!",
    "what is your name": "I'm a simple chatbot created in Python.",
    "help": "Sure! I'm here to help. Ask me anything.",
    "default": "I'm sorry, I don't understand that. Could you please rephrase?"
}

def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    while True:
       
        user = input("You: ").lower()

        if user == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        
        reply = reply.get(user, reply["default"])
        print(f"Chatbot: {reply}")


chatbot()

