import sys
import random
from termcolor import colored

def show_cows():
    cows = [
        """  _____
 /     \\
| () () |
 \\  ^  / 
  ||||| 
  ||||| """,
        """  ______ 
 /      \\
|  (o) (o) 
|   \\/   
 \\______/
 """,
        """   __
  (oo)
 /------\\
/ |    || 
*  ||----||
   ^^    ^^ """,
        """   /~\\
  ( oo|
  _\\=__/
 /   \\
|     |
 ||_||""",
        """    ________
   /  ()  ()\\
  |    |    |
  |  __|__  |
   \\______/
    |    |
    |    |""",
        """   /\\_/\\
  ( o.o )
   > ^ < """,
        """   _____
  /      \\
 |  (o) (o)
 |    < 
 |  \___/
 |______""",
        """   /\\_/\\
 ( o o )
  (  "  )""",
        """  _____
 /     \\
| () () |
|  --  |
 \\_____/""",
        """   ________
  /  (o)   \\
 |    |    |
 |  __|__  |
  \\______/
   |    |
   |____|
""",
        """    _____
   /      \\
  |  (o)  (o)
  |   ___  
  |______|
""",
        """   ____ 
  /    \\
 |  O  O |
 |   _   |
 |_______|""",
        """   /\\_/\\
  ( o.o )
   (   )""",
        """  _______
 /  ()  ()\\
|    /    |
|   |_____|""",
        """   /\\_/\\
  ( o o )
   (  .  )""",
        """   _____
  /     \\
 |  (o)  |
 |   -   |
  \\_____/
""",
        """  _____
 /     \\
|  (o) (o)
|   ----
 \\_____/""",
        """   /~\\
  ( o o )
  /  |  \\
 /   |   \\ """,
        """   _____
  /     \\
 | () () |
 |______|
 |      |""",
        """  _______
 /  ()  ()\\
|  __   __|
| /  \\ /  \\
""",
        """   /~\\
  ( o.o )
   (   )""",
        """   /\\_/\\
  ( o o )
   (  ^  )
   (____)"""
    ]
    return cows

def create_speech_bubble(text, cow_art):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    bubble = [" " + "_" * (max_len + 2) + " "]
    bubble += ["/ " + line.ljust(max_len) + " \\" for line in lines]
    bubble.append("\\_" + "_" * (max_len + 2) + "/")
    bubble.append(cow_art)
    return '\n'.join(bubble)

def print_cow(cow_index):
    cows = show_cows()
    if 0 <= cow_index < len(cows):
        return cows[cow_index]
    else:
        return "Invalid cow index."

def show_help():
    help_text = """
Usage:
  python cowser.py <command>

Commands:
  <user_name>    Greet the user with a random ASCII art cow.
  help           Show this help message.
  list           List all available ASCII art options.
"""
    print(colored(help_text, 'yellow'))

def list_all_cows():
    cows = show_cows()
    for i, cow in enumerate(cows):
        print(f"Option {i}:")
        print(cow)
        print()

def main():
    if len(sys.argv) != 2:
        show_help()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'help':
        show_help()
    elif command == 'list':
        list_all_cows()
    else:
        user_name = command
        cows = show_cows()
        random_cow_index = random.randint(0, len(cows) - 1)
        greeting = f"Hi {user_name}!"
        cow_art = print_cow(random_cow_index)
        bubble_output = create_speech_bubble(greeting, cow_art)
        print(colored(bubble_output, 'cyan'))

if __name__ == "__main__":
    main()
