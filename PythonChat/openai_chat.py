from openai import OpenAI
from config import OPENAI_API_KEY

api_key = OPENAI_API_KEY
client = OpenAI(api_key=api_key)

def chat_with_openai(user_input, chat_history):
    chat_history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *chat_history
        ]
    )
    ai_response = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": ai_response})
    return ai_response