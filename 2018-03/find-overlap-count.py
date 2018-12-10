#!/usr/bin/env python3

## Path info
# import sys
# for p in sys.path:
#   print(p)

## Logging
import logging as log
import coloredlogs

## Logging Setup
FORMAT = '%(asctime)-15s %(filename)s %(lineno)d: %(message)s'
coloredlogs.install(fmt=FORMAT,level=log.DEBUG)

## Objects
from Fabric import Fabric


fabric = Fabric()
print(fabric.to_string())

with open('input.txt') as x: lines = x.readlines()

result = 0

for line in lines:

  string = line.strip()

  print(string)

  fabric.parse_claim(string)

  print(fabric.to_string())

  raise SystemExit
  sys.exit()

