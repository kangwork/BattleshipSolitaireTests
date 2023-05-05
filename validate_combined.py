import copy
import random
import time
import queue
import sys
import os

# Validation script for CSC384 A3 : battle.py
# Change input_easy1.txt, output_easy1.txt and solution_easy1.txt to run
# other test inputs.
#

if __name__ == '__main__':
# Invoke the shell command to test the checkers solver
    # files = ["easy1", "easy2", "medium1", "medium2", "hard1", "hard2", "3"]
    files = ["easy6", "easy9", "medium3", "medium5", "hard3", "hard4", "hard5"]
    i = 0
    passed = [True] * len(files)
    for file in files:
        print(f"Input file: puz_{file}.txt, output file: output_{file}.txt")
        start = time.time()
        os.system(f"python3 battle.py puz_{file}.txt output_{file}.txt")
        end = time.time()
        time_took = end - start
        print('실행 시간: {}초'.format(time_took))
        output_read = open(f"output_{file}.txt", "r")
    #     solution_read = open(f"solution_{file}.txt", "r")

    #     output_lines = output_read.readlines()
    #     solution_lines = solution_read.readlines()

    #     for index in range(1, len(output_lines)):
    #         if output_lines[index].strip() != solution_lines[index].strip():
    #             print(f"Line {index + 1}: " f"Expected <{output_lines[index].strip()}> " f"Encountered <{solution_lines[index].strip()}>\n")
    #             passed[i] = False
    #             break
    #     i += 1
    # for i in range(len(passed)):
    #     result = "Passed" if passed[i] else "Failed"
    #     print(f"{files[i]}: {result}")
    #     print("Finished all tests.")
