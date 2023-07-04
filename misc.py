# The slowprint(string) function is not mine, I searched how to make this function online and got it from https://stackoverflow.com/a/54472904
import random
from misc import *

def read(filename):
  in_file = open("data/" + filename + ".txt", "r")
  line = in_file.readline()
  line_list = line.split(" ")
  in_file.close()
  return " ".join(line_list)

def write(filename, string):
  in_file = open("data/" + filename + ".txt", "w")
  print(string, file = in_file, end=" ")
  in_file.close()

def openfile(filename):
  file = open("data/" + filename + ".txt", 'r')
  list = []
  for line in file:
    line = line.strip()
    statement = line.split(',')
    list.append(statement)
  file.close()
  return list

def choosestatement(filename):
  list = openfile(filename)
  index = random.randrange(len(list))
  statement = list[index]
  return " ".join(statement)