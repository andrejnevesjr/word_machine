import os
from time import time
from typing import List
from queue import LifoQueue
import timeit
from aux.read_file import ReadFile

def word_commands(data: List) -> int:
    myStack = LifoQueue()
    list_index = 0
    list_size = len(data)-1

    while list_index <= list_size:

        current_value = data[list_index]

        if (current_value == "DUP" and myStack._qsize() > 0):

            top_stack = myStack.get()
            myStack.put(top_stack)
            myStack.put(top_stack)

        elif (current_value == "POP" and myStack._qsize() > 0):
            myStack.get()

        elif (current_value == "+" and myStack._qsize() > 1):

            first_value = myStack.get()
            second_value = myStack.get()
            myStack.put(first_value + second_value)

        elif (current_value == "-" and myStack._qsize() > 1):

            first_value = myStack.get()
            second_value = myStack.get()
            myStack.put(first_value - second_value)

        else:
            try:
                myStack.put(int(current_value))
            except (ValueError, TypeError):
                return -1

        list_index += 1

    return myStack.get()


def main():

    start = timeit.default_timer()
    # print("Starting the Challenge!")

    rfile = ReadFile()

    # Read file
    data, expected_result = rfile.read_file("/resource/tests.txt")

    result = word_commands(data[1])

    # print("Finishing the Challenge!")
    stop = timeit.default_timer()
    elapsed_time = stop - start
    print("Program Executed in "+str(elapsed_time))


if __name__ == '__main__':
    main()
