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
            print("ChatPy: I'm ChatPy, your AI Friend!")
        elif "help" in user_input or "ask" in user_input:
            print("ChatPy:Hey I cant Help You at this Moment as i am just a basic Chatbot.")
        else:
            print("ChatPy:Sorry i am not trained to answer this as far now.")

# run the code
chatbot()

