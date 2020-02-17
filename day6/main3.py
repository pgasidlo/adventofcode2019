import sys

children = {}

for line in open("input.txt"):
    points = line.rstrip().split(')')
    if points[0] not in children:
        children[points[0]] = []
    if points[1] not in children:
        children[points[1]] = []
    children[points[0]].append(points[1])

def summe(i, depth):
    global children
    sum = depth
    for j in children[i]:
        sum = sum + summe(j, depth + 1)
    return sum

print "orbits =", summe('COM', 0)

