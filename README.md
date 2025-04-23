# Binary Oracle

🔮 **Binary Oracle** is a Python-based application that answers Yes/No questions. It uses a deterministic algorithm to provide consistent answers for the same question on the same day.

## Features

- Stores a history of questions and answers in a JSON file.
- Detects and retrieves answers for similar questions asked on the same day.
- Provides a fun "thinking" animation for user interaction.

## Project Structure

```
question.py          # Main application script
data/
    questions.json   # JSON file storing question history
```

## Requirements

- Python 3.7 or higher
- The following Python libraries:
  - `Levenshtein`
  - `readline`

## Installation

1. Clone this repository or copy the files to your local machine.
2. Install the required Python libraries:
   ```sh
   pip install python-Levenshtein
   ```

## How to Run

1. Open a terminal and navigate to the project directory.
2. Run the application:
   ```sh
   python question.py
   ```
3. Ask Yes/No questions and enjoy the answers!

## Environment Variables

- `THINK_DATA`: Set this environment variable to specify a custom directory for storing the `questions.json` file. If not set, the default directory is `./data`.

## Example Usage

```plaintext
🔮 Welcome to the Binary Oracle...
(Type 'exit' to quit)

🧠 Ask a Yes/No question: Should I buy a new car?
🤖 Thinking...
💬 Answer: Yes

🧠 Ask a Yes/No question: Should I buy a new car?
🤖 Thinking...
🔁 Found similar question from today.
💬 Answer: Yes
```

## License

This project is open-source and available under the MIT License.
