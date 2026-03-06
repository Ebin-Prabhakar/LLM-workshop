import sys
from gym import ask_gym_assistant

def main():
    question = sys.stdin.read().strip()
    if question:
        print(ask_gym_assistant(question), end="")

if __name__ == "__main__":
    main()
