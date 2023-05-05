import copy
import random
import time
import queue
import sys
import os

# Validation script for CSC384 A3 : battle.py
# Change input_easy1.txt, output_easy1.txt and solution_easy1.txt to run
#    other test inputs.
# 인풋 이지1  -- 18.27 초
# 인풋 이지2  -- 39초
# 인풋 미디움1 --0.315
# 인풋 미디움2 -- 1.37
# 인풋 하드1  -- 7.92초 -- 7.75초(1인 걸 빼니까) -- 1인 걸 넣으니까 8.87초 -- 8.16초  -- (+5)하니까 1.43초
# 인풋 하드2 -- 1.28초 -- 8 -- 8.63초(1인 걸 빼니까) -- 1인 걸 넣으니까 10초 -- 7초대(+5)하니까
# henry input3 --
# henry input 4 --

if __name__ == '__main__':
  # Invoke the shell command to test the checkers solver
  print("BATTLE_VALIDATE")
  os.system("python3 battle.py input10.txt output.txt")

  output_read = open("output.txt", "r")
  solution_read = open("sol10.txt", "r")

  output_lines = output_read.readlines()
  solution_lines = solution_read.readlines()
  passed = True

  for index in range(1, len(output_lines)):
    if output_lines[index].strip() != solution_lines[index].strip():
      print(f"Line {index + 1}: "
                             f"Expected <{output_lines[index].strip()}> "
                             f"Encountered <{solution_lines[index].strip()}>\n")
      passed = False
      break

  if passed:
    print("Battleship output matches solution file.")
