from bot.chatbot import generate_response

def main():
    print("Chatbot is ready! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            print("Exiting chat...")
            break
        
        response = generate_response(user_input)
        print(f"Bot: {response}")
        
if __name__ == "__main__":
    main()
