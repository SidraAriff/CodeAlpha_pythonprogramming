def chatbot():
    print("Hello! I'm ChatPy. Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("ChatPy: Goodbye! Have a great day.")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("ChatPy: Hello! How can I help you?")
        elif "how are you" in user_input:
            print("ChatPy: I'm just a program, but I'm doing fine. Thanks!")
        elif "your name" in user_input:
            print("ChatPy: I'm ChatPy, your friendly chatbot!")
        elif "help" in user_input or "ask" in user_input
            print("ChatPy: Sure! Ask me anything about Python or general questions.")
        else:
            print("ChatPy: I'm sorry, I don't understand that yet.")

# Run the chatbot
chatbot()
