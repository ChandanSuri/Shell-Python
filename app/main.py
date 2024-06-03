import sys


def main():
    print("Logs from your program will appear here!")

    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    input()


if __name__ == "__main__":
    main()
