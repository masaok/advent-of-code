#!/usr/bin/env python3

with open('input.txt') as x: lines = x.readlines()

result = 0

freqs = {}

while True:
  for line in lines:
    print(line)
    string = line.strip()
  
    operation = string[:1]
  
    number = string[1:]
  
    if operation == "+":
      result += int(number)
  
    if operation == "-":
      result -= int(number)
  
    if result not in freqs:
      freqs[result] = 0
  
    freqs[result] += 1
  
    print("FREQ: " + str(freqs[result]))
  
    if freqs[result] > 1:
      print("END")
      print(result)
      raise(SystemExit)
  
print("ALL DONE")
print(result)
