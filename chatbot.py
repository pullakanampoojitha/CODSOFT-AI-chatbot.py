import random

# Define a list of predefined user queries and their corresponding responses
responses = {
    "hello" : ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a chatbot, but I'm here to help!", "I don't have feelings, but thanks for asking!"],
    "what's your name": ["I'm just a chatbot, you can call me AIChatbot.", "I'm AIChatbot, nice to meet you!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "how is todays weather" :["The weather is sunny today.","The weather is too cool today!.", "It's rainy outside.", "I'm not sure about the weather. You can check a weather website for accurate information."],
    "what time is it" :["Sorry!,I don't have access to real-time information. Please check the time on your device."],
    "how old are you" :["I don't have an age or birthdate because I'm a computer program"],
    "what is the latest news ":["I'm not currently equipped to provide the latest news. You can check a news website or app for up-to-date information."],
    "tell me a joke" :[ "Why did the scarecrow win an award? Because he was outstanding in his field!","Sure! Here's one: Why don't scientists trust atoms? Because they make up everything!","Why did the computer keep freezing? Because it left its Windows open!"],
    "thank you" :["Its my pleasure!","Thank you"],
    "default": ["I'm sorry, I don't understand. Can you please rephrase your question?", "I'm not sure how to respond to that."]
}

# Main function to handle user input and provide responses
def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if the user's input matches any predefined queries
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    
    # If no predefined query is matched, provide a default response
    return random.choice(responses["default"])

# Chatbot interaction loop
print("Chatbot: Hi! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)