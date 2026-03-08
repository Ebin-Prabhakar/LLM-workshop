import sys
from gym import ask_gym_assistant


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stdin, "reconfigure"):
        sys.stdin.reconfigure(encoding='utf-8')

    if not sys.stdin.isatty():
        question = sys.stdin.read().strip()
    else:
        question = input("Enter your fitness question: ").strip()

    if question:
        print(ask_gym_assistant(question), end="")


if __name__ == "__main__":
    main()