#!/usr/bin/env python3

## Logging
import logging as log
import coloredlogs

from pprint import pprint
from pprint import pformat

"""
#1 @ 287,428: 27x20
#2 @ 282,539: 20x10
#3 @ 550,118: 20x23

ID @ col_off,row_off: width x height
"""

class Fabric:

  def __init__(self):
    self.side = 500
    self.width, self.height = self.side, self.side
    self.fabric = [[0 for x in range(self.width)] for y in range(self.height)] 

  def add_claim(self, claim):
    print("add")

  def parse_claim(self, claim):
    ids, at, offsets, dimensions = claim.split(' ')
    
    offsets = offsets.strip()
    offsets = offsets[:-1]
    print("offsets: " + offsets)
    col_offset, row_offset = offsets.split(',')

    log.info("dimensions: " + dimensions)
    width, height = dimensions.split('x')

    col_offset = int(col_offset)
    row_offset = int(row_offset)

    width = int(width)
    height = int(height)

    for dx in range(width):
      x = col_offset + dx + 1

      for dy in range(height):
        y = row_offset + dy + 1

        print("x: " + str(x) + ", y: " + str(y))
        self.fabric[x][y] = 1


  def to_string(self):
    
    result = ""
    
    for x in range(len(self.fabric)):
      print("x: " + str(x))
      for y in range(len(self.fabric[x])):
        result += str(self.fabric[x][y])
      result += "\n"

    return result