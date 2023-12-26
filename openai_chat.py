# openai_chat.py
from openai import OpenAI
from config import OPENAI_API_KEY

api_key = OPENAI_API_KEY
client = OpenAI(api_key=api_key)

def chat_with_openai(user_input, chat_history):
    # Add the user input to the chat history
    chat_history.append({"role": "user", "content": user_input})

    # Make the API call with the chat history
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *chat_history
        ]
    )

    # Get the AI response from the API
    ai_response = response.choices[0].message.content

    # Add the AI response to the chat history
    chat_history.append({"role": "assistant", "content": ai_response})

    return ai_response
