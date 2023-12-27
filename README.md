# PythonChat

### File Descriptions

#### `src/openai_chat/openai_chat.py`
This module handles interactions with the OpenAI API.

#### `src/chat_logger/chat_logger.py`
This module provides functions to log and save chat history.

#### `src/main.py`
The main script that initiates the chat loop.

#### `config/config.py`
Configurations, such as API keys, are stored in this file.

#### `data/chat_history.txt`
A file to store the chat history.

### How to Run

1. Ensure you have the required dependencies installed. You can install them using `pip install -r requirements.txt`.
2. Open the `config/config.py` file and replace the placeholder in `OPENAI_API_KEY` with your actual OpenAI API key.
3. Run `main.py` to start the chat.

### Usage

- Enter your message when prompted with "You:".
- Type "exit" to end the conversation.

### Note

- The chat history is saved to `data/chat_history.txt` after each conversation.

Make sure to replace `"YOUR_ACTUAL_OPENAI_API_KEY"` in `config/config.py` with your valid OpenAI API key.
