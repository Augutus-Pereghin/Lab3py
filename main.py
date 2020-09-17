# Author: Augustus Perseghin agp5191
# Collaborator: Zehao Liu zql5426@psu.edu
# Collaborator: Kieran Murdocca kkm5754@psu.edu
# Collaborator: Nidhi Swamy nms6241@psu.edu
# Section: 4
# Breakout: 15

def sum_n(n):
  if n > 0:
    return n + sum_n(n-1)
  else:
    return 0

def print_n(string, n):
  print("string")
  if n > 0:
    print_n(string, n-1)
  return

def run:
  input("Enter an int: ")