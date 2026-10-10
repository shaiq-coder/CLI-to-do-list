# 💻 Python CLI To-Do App

**BLUF:** A lightweight, persistent command-line interface (CLI) To-Do List application built in Python. 

This project demonstrates practical data persistence using File I/O operations without relying on external databases. It was built to solidify foundational programming concepts including control flow, exception handling, and context managers.

## 🚀 Features
* **Persistent Storage:** Tasks are saved to a local `tasks.txt` file, meaning your data survives after closing the program.
* **Input Validation:** Prevents crashes using `try-except` blocks if non-numeric data is entered during deletion.
* **Dynamic Indexing:** Automatically numbers tasks sequentially using Python's `enumerate()` function.
* **Clean UI:** Minimalist terminal-based menu for rapid task management.

## 🛠️ Tech Stack & Concepts
* **Language:** Python 3
* **Core Concepts:** 
  * File I/O (`read`, `write`, `append`)
  * Context Managers (`with open`)
  * Error Handling (`ValueError` exceptions)
  * Module imports (`os` for file path verification)

## ⚙️ How to Run
1. Clone the repository: `git clone https://github.com/yourusername/CLI-ToDo-App.git`
2. Navigate to the directory: `cd CLI-ToDo-App`
3. Run the script: `python todo.py`