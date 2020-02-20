from functools import reduce
from textwrap import wrap

maxW = 25
maxH = 6

stream = open("input.txt").read().rstrip()

layers = []

i = 0
layer = ""
for char in stream:
  layer = layer + char
  i = (i + 1) % (maxW * maxH)
  if (i == 0):
    layers.append(layer)
    layer = ""

best = {}

for layer in layers:
  cur = { 'layer': layer }
  for char in layer:
    cur["s" + char] = cur.get("s" + char, 0) + 1
  if (not best or (best['s0'] > cur['s0'])):
    best = cur

print "part1 = ", best['s1'] * best['s2']

result = ""

for i in range(maxW * maxH):
  for layer in layers:
    if (layer[i] == '0'):
      result = result + ' '
      break
    elif (layer[i] == '1'):
      result = result + '#'
      break

print "part2 =\n", "\n".join(wrap(result, maxW))