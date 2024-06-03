import sys

VALID_COMMANDS = set()

def main():

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        if command not in VALID_COMMANDS:
            sys.stdout.write(f"{command}: command not found\n")
            continue

if __name__ == "__main__":
    main()
