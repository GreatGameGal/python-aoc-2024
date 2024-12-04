import sys

inputFile = open(sys.path[0] + "/input.txt")
input = inputFile.read()
inputFile.close()

input = input.split("\n")

lists = [[], []]
for line in input:
    if line == "":
        continue
    split = line.split(" ")
    lists[0].append(split[0])
    lists[1].append(split[-1])

lists[0].sort()
lists[1].sort()

total = 0
for i in range(len(lists[0])):
    total += abs(int(lists[0][i]) - int(lists[1][i]))

print("Solution 1: " + str(total))

similarity = 0
for val in lists[0]:
    similarity += int(val) * lists[1].count(val)

print("Solution 2: " + str(similarity))
