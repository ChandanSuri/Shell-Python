import sys

VALID_COMMANDS = set("exit")

def main():

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        commandParams = command.split(" ")
        commandName, args = commandParams[0], commandParams[1]

        if commandName not in VALID_COMMANDS:
            sys.stdout.write(f"{commandName}: command not found\n")
            continue

        if commandName == "exit" and args == "0":
            break

if __name__ == "__main__":
    main()
