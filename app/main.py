import sys

VALID_COMMANDS = set("exit")

def main():

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        commandParams = command.split(" ")
        commandName = commandParams[0]
        args = []

        for argument in range(1, len(commandParams)):
            args.append(argument)

        if commandName not in VALID_COMMANDS:
            sys.stdout.write(f"{commandName}: command not found\n")
            continue

        if commandName == "exit" and args[0] == "0":
            break

if __name__ == "__main__":
    main()
