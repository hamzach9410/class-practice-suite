import sys
import random

def get_response(user_input):
    user_input = user_input.lower().strip()
    
    responses = {
        "hello": ["Hi there!", "Hello!", "Greetings!", "How can I help you today?"],
        "how are you": ["I'm doing well, thank you!", "I'm a bot, but I'm feeling great!", "Everything is systems go!"],
        "what is your name": ["I am the Class Practice Chatbot.", "You can call me CP-Bot.", "I don't have a human name, but Chatbot works."],
        "bye": ["Goodbye!", "Have a nice day!", "See you later!"],
        "default": ["That's interesting!", "Tell me more about that.", "I'm not sure I understand, but I'm listening.", "Can you elaborate?"]
    }

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

def main():
    print("Welcome to the AI Chatbot Demo!")
    print("Type 'exit', 'quit', or 'bye' to end the conversation.")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Bot: " + get_response("bye"))
                break
            
            response = get_response(user_input)
            print(f"Bot: {response}")
            
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nBot: Goodbye!")
            break

if __name__ == "__main__":
    main()
