from openai_chat import chat_with_openai
from chat_logger import save_chat_history

chat_history = []

print("Welcome to the ChatBot! Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    ai_response = chat_with_openai(user_input, chat_history)
    print(f"AI: {ai_response}")

save_chat_history(chat_history)