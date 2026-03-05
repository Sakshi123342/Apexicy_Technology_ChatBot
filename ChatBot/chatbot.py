# print("hello sakshi")
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("you: ").lower()

        if user == "hello":
            print("Chatbot: Hi!")

        elif user == "how are you":
            print("Chatbot: I'm fine,thanks!")

        elif user == "what is your name":
            print("Chatbot: I am a simple chatbot.")

        elif user == "bye":
            print("Chatbot: Sorry,I don't understand.")
chatbot()
