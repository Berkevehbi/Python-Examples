# Clipboard Text Manager

This simple Python script serves as a clipboard text manager. It allows users to store word pairs in a text database file (`database.txt`) and easily copy sentences associated with specific words to the clipboard.

## How It Works

1. **Initialization:**
   - The program starts by checking for the existence of a `database.txt` file.
   - If the file exists, it loads the data into a dictionary called `texts`.
   - If the file doesn't exist, it creates an empty `database.txt` file.

2. **Text Registration:**
   - Users can register new word pairs by providing a word and a corresponding sentence.
   - The program updates both the `texts` dictionary and the `database.txt` file.

3. **Clipboard Copy:**
   - Users can input a word, and if it exists in the `texts` database, the associated sentence is copied to the clipboard using the Pyperclip library.

4. **Looped Operation:**
   - The program runs in a loop to provide a continuous user interface.
   - Users can keep interacting with the program without reopening it until they choose to exit.

## Usage

1. **Adding New Text:**
   - When prompted "What do you want to copy?" enter a word.
   - If the word exists in the database, the corresponding sentence will be copied to the clipboard.
   - If the word is not in the database, you will be prompted to add it along with the corresponding sentence.

2. **Exiting the Program:**
   - To exit the program, simply enter `0` when prompted "What do you want to copy?"

## Getting Started

1. **Requirements:**
   - Python 3

2. **Run the Program:**
   - Open a terminal and navigate to the project directory.
   - Run the program using the following command:
     ```bash
     python main.py
     ```
