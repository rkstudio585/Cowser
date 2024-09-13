# Cowser 🐄
---
![Logo](logo.svg)

---
Welcome to **Cowser**, a fun command-line tool written in Python that displays ASCII art cows with customizable greetings! This project combines the classic `cowsay` tool functionality with Python scripting to provide a unique and interactive experience.

## Features 🌟

- **Greet Users**: Personalize your greeting with a random ASCII art cow.
- **Help Command**: Provides usage instructions and available commands.
- **List ASCII Art**: Displays all available ASCII art options.
- **Customizable**: Easily extend with more ASCII art designs.

## Getting Started 🚀

### Prerequisites

- Python 3.x installed on your system.
- `termcolor` library for colored output.

### Installation

1. **Clone the Repository**

   To get started, clone the repository to your local machine:

   ```bash
   git clone https://github.com/rkstudio585/Cowser
   cd Cowser
   ```
2. Install Dependencies

Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```
3. Make the Bash Script Executable

If you want to use the provided cowset script, make it executable:
```bash
chmod +x cowset
```

Usage 📜

Using the Python Script

Run the cowser.py script with the following commands:

Greet a User
```python
python main.py <user_name>
```
Replace <user_name> with the name you want to greet. This will show a random ASCII art cow with a personalized greeting.

Show Help
```python
python main.py help
```
Displays usage instructions and available commands.

List All ASCII Art
```python
python main.py list
```
Lists all available ASCII art options.


Using the Bash Script

Alternatively, you can use the cowset bash script:

Greet a User
```bash
./cowset <user_name>
```
Show Help
```bash
./cowset help
```
List All ASCII Art
```bash
./cowset list
```

Adding More ASCII Art 🎨

To add more ASCII art designs:

1. Open main.py.
```python
nano main.py
```

2. Update the show_cows() function with additional ASCII art strings.



Customization and Hacks ✨

1. Enhanced Output: Use termcolor to add color and style to your output.


2. Interactive Commands: Modify main.py to include more interactive features.



Contributing 🤝

Contributions are welcome! Please open an issue or submit a pull request on GitHub if you have suggestions or improvements.


---

Have fun with Cowser! 🎉

| Command         | Description                                    |
|-----------------|------------------------------------------------|
| `<user_name>`   | Greet the user with a random ASCII art cow.   |
| `help`          | Show usage instructions.                      |
| `list`          | List all available ASCII art options.         |
