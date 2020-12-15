version = "0.0.1"
commands = ["help", "version", "set_key", "get_key", "trigger"]


def shell():
    print("STABATDATA - "+version)
    print("Self-deleting data format shell")
    print("(C) 2020, All rights reserved.")
    while True:
        command = input("\n\t >> ")
        run_command(command)


def run_command(command):
    if command in commands:
        if command == "help":
            for query in commands:
                print("\t "+query)

        elif command == "version":
            print("\t "+version)

        return 0
    else:
        print("\t Invalid command - Please try again!")


if __name__ == "__main__":
    shell()
