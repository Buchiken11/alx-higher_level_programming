#!/usr/bin/python3
import sys

def print_arguments():
    # The script name is at sys.argv[0]
    script_name = sys.argv[0]
    print(f"Script name: {script_name}")

    # Number of command-line arguments
    num_arguments = len(sys.argv) - 1  # Subtract 1 for the script name
    print(f"Number of arguments: {num_arguments}")

    # Print each command-line argument
    print("Arguments:")
    for index, arg in enumerate(sys.argv[1:], start=1):
        print(f"  {index}: {arg}")

if __name__ == "__main__":
    print_arguments()
