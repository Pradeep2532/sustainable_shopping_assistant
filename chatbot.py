# chatbot.py
from nlu import classify_intent, get_response_for_intent

def get_chatbot_response(user_input):
    """
    Processes user input and returns a chatbot response.
    """
    intent, item = classify_intent(user_input)
    response = get_response_for_intent(intent, item)
    return response

def run_cli_chatbot():
    """
    Runs the chatbot in a command-line interface.
    """
    print("Welcome to the Sustainable Shopping Assistant! 🌍")
    print("I can help you with eco-friendly alternatives, food waste tips, environmental impact of items, or general sustainability tips.")
    print("Type 'quit' or 'exit' to end the conversation.")

    while True:
        user_input = input("\nYou: ").strip() # Remove leading/trailing whitespace
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye! Happy sustainable shopping! 🌱")
            break
        
        response = get_chatbot_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    run_cli_chatbot()