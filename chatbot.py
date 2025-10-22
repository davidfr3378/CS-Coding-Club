print("🤖 ChatBot: Hi! I'm PyBot. Type 'bye' to exit.")

# Start with a few default responses
responses = {
    "hello": "Hey there! Nice to meet you!",
    "how are you": "I’m feeling electric ⚡ thanks for asking!",
    "weather": "I can’t feel the weather, but I hope it’s sunny where you are!"
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("🤖 ChatBot: Goodbye! Talk to you later!")
        break

    # If the chatbot knows the response
    elif user_input in responses:
        print("🤖 ChatBot:", responses[user_input])

    # If it doesn’t know the response — learn it
    else:
        print("🤖 ChatBot: Hmm... I don’t know how to respond to that.")
        new_response = input("🤖 ChatBot: What should I say next time for that? ")
        responses[user_input] = new_response
        print("🤖 ChatBot: Got it! I’ll remember that for later.")

