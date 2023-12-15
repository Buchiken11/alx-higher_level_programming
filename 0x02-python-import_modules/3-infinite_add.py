#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def add_arg(command_line):
        #try:
            result = sum(map(int, command_line))
            return result
        except ValueError:
            print("Error: All arguments must be integers")
            return None

    command_line = sys.argv[1:]

    if command_line:
        result = add_arg(command_line)
        if result is not None:
            print("{}".format(result))
    else:
        print("No command line argument found")
