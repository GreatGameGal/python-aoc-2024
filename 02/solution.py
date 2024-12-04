import sys
import math

inputFile = open(sys.path[0] + "/input.txt", "r")
input = inputFile.read()

def list_safe(list, lastNum = None, dir = None, damped = True):
    if len(list) == 0:
        return False
    if len(list) == 1:
        return True
    if lastNum == None:
        return list_safe(list[1:], list[0], None, damped)
    diff = list[0] - lastNum
    if dir == None:
        dir = math.copysign(1, diff)
    if diff * dir < 1 or diff * dir > 3:
        if damped:
            return False
        damped = True
        return list_safe(list[1:], list[1], dir, damped)
    return list_safe(list[1:], list[0], dir, damped)

lines = input.split('\n')
while "" in lines:
    lines.remove("")
lines = [[int(val) for val in line.split(' ')] for line in lines]

safe = sum([list_safe(line) for line in lines])
safe2 = sum([list_safe(line, damped = False) for line in lines])

print("Solution 1: ", safe)
print("Solution 2: ", safe2)
