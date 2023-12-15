#!/usr/bin/python3

#  Prints the number of and the list of its arguments

if __name__ == "__main__":

    import sys


    name_of_arguments = sys.argv

    number_of_arguments = len(name_of_arguments) - 1


    if number_of_arguments > 1:

        print("{} arguments:".format(number_of_arguments))

        for i in range(1, number_of_arguments + 1):

            print("{}: {}".format(i, name_of_arguments[i]))


    elif number_of_arguments == 0:

        print("{} arguments.".format(number_of_arguments))


    else:

        print("{} argument:".format(number_of_arguments))

        print("{}: {}".format(size, name_of_arguments[1]))
