import os
import sys
import timeit

sys.path.append(os.path.join(os.path.dirname(__file__),'..','resource')) 
# sys.path.append(os.path.join(os.path.dirname(__file__),'..','..','resource', '0_common'))  

from luanStack import Solution
from aux.read_file import ReadFile

def main():
    
    start = timeit.default_timer()
    # print("Starting the Challenge!")
    
    read_file = ReadFile()
    run_commands = Solution()

    #Read file to List
    data, result = read_file.read_file("/resource/tests.txt")
    
    # Run commmands
    run_commands.solve(data[0])

    # print("Finishing the Challenge!")
    stop = timeit.default_timer()
    elapsed_time = stop - start
    print("Program Executed in "+str(elapsed_time))


if __name__ == "__main__":
    main()