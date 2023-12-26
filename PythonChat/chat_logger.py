def save_chat_history(chat_history, filename="chat_history.txt"):
    with open(filename, "w") as file:
        for entry in chat_history:
            file.write(f"{entry['role']}: {entry['content']}\n")
