from agent import reasoning, memory, tools, rl, safety
from tools import emailer
from rl import feedback
from safety import validation

def main():
    print("Hello, I am your AI assistant.")
    while True:
        user_input = input("What would you like help with? (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Have a great day!")
            break


if __name__ == "__main__":
    main()