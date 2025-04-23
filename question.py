import hashlib
import datetime
import random
import time
import os
import json
import readline
from Levenshtein import ratio

# Environment variable for data file
DATA_PATH = os.environ.get("THINK_DATA", "./data")
DATA_FILE = os.path.join(DATA_PATH, "questions.json")

os.makedirs(DATA_PATH, exist_ok=True)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(history):
    with open(DATA_FILE, "w") as f:
        json.dump(history, f, indent=2)

def get_today_str():
    return datetime.datetime.now().strftime('%Y-%m-%d')

def find_similar_today(question, history, threshold=0.9):
    today = get_today_str()
    for entry in history:
        if ratio(question.lower(), entry['question'].lower()) >= threshold:
            if entry['timestamp'].startswith(today):
                return entry
    return None

def generate_decision(question, salt=None):
    now = datetime.datetime.now()
    if salt is None:
        salt = random.randint(100000, 999999)
    seed_string = f"{question}-{now.strftime('%Y-%m-%d')}-{salt}"
    hash_digest = hashlib.sha512(seed_string.encode()).hexdigest()
    hash_number = int(hash_digest[:16], 16)
    decision = "Yes" if hash_number % 2 == 0 else "No"
    return decision, salt, now

def thinking_animation():
    print("🤖 Thinking", end='', flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end='', flush=True)
    print("\n")

def setup_history(history):
    for entry in history:
        readline.add_history(entry["question"])

def main():
    history = load_data()
    setup_history(history)

    print("🔮 Welcome to the Binary Oracle...\n(Type 'exit' to quit)\n")

    while True:
        try:
            question = input("🧠 Ask a Yes/No question: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Goodbye!")
            break

        if question.lower() == "exit":
            print("👋 Goodbye!")
            break

        if not question:
            continue

        similar_today = find_similar_today(question, history)

        thinking_animation()

        if similar_today:
            print(f"🔁 Found similar question from today.")
            print(f"💬 Answer: {similar_today['answer']}\n")
        else:
            answer, salt, timestamp = generate_decision(question)
            entry = {
                "question": question,
                "answer": answer,
                "timestamp": timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                "salt": salt
            }
            history.append(entry)
            readline.add_history(question)
            save_data(history)
            print(f"💬 Answer: {answer}\n")

if __name__ == "__main__":
    main()
