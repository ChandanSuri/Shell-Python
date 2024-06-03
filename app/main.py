import sys
import os

VALID_COMMANDS = set(
    [
        "exit",
        "echo",
        "type"
    ]
)

def main():
    pathEnvVar = os.environ.get("PATH")
    paths = pathEnvVar.split(":")

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        commandParams = command.split(" ")
        commandName = commandParams[0]
        args = []

        for idx in range(1, len(commandParams)):
            args.append(commandParams[idx])

        if commandName not in VALID_COMMANDS:
            sys.stdout.write(f"{commandName}: command not found\n")
            continue

        if commandName == "exit" and args[0] == "0":
            break

        if commandName == "echo":
            toPrintString = " ".join(args)
            sys.stdout.write(f"{toPrintString}\n")
        elif commandName == "type":
            commandToCheck = args[0]
            commandPath = getExecPath(paths, commandToCheck)

            if commandToCheck in VALID_COMMANDS:
                sys.stdout.write(f"{commandToCheck} is a shell builtin\n")
            elif commandPath is not None:
                sys.stdout.write(f"{commandToCheck} is {commandPath}\n")
            else:
                sys.stdout.write(f"{commandToCheck} not found\n")

def getExecPath(paths, commandToCheck):
    commandPath = None

    for path in paths:
        if os.path.isfile(f"{path}/{commandToCheck}"):
            commandPath = f"{path}/{commandToCheck}"
            break

    return commandPath

if __name__ == "__main__":
    main()
