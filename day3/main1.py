import re
import json

moves = []

with open("input2.txt") as f:
  moves = f.read().splitlines()
moves = map(lambda x: x.split(","), moves)

def moves2lines(moves):

  lines = {'H': [], 'V': []}

  x = 0
  y = 0

  for move in moves:
    m = re.search(r"^([RLUD])(\d+)$", move)
    direction = m.group(1)
    delta = int(m.group(2))

    dx = 0
    dy = 0
    box = None
    dd = None

    if (direction == 'R'):
      dx = delta
      box = 'H'
      dd = '+'
    elif (direction == 'L'):
      dx = -delta
      box = 'H'
      dd = '-'
    elif (direction == 'U'):
      dy = delta
      box = 'V'
      dd = '+'
    elif (direction == 'D'):
      dy = -delta
      box = 'V'
      dd = '-'
    else:
      raise Exception("Invalid direction = ", direction)

    s = {'x': x, 'y': y }

    x = x + dx
    y = y + dy

    e = {'x': x, 'y': y }

    print "move =", move, "s =", s, "-> e =", e, "box = ", box

    if (dd == '+'):
      lines[box].append({'s': s, 'e': e, 't': box, 'm': move})
    else:
      lines[box].append({'s': e, 'e': s, 't': box, 'm': move})

  return lines

def cross(line1, line2):
  if (
    line1['t'] == 'H' and
    line2['t'] == 'V' and
    line1['s']['x'] < line2['s']['x'] and
    line1['e']['x'] > line2['e']['x'] and
    line2['s']['y'] < line1['s']['y'] and
    line2['e']['y'] > line1['e']['y']
  ):
    return { 'x': line2['s']['x'], 'y': line1['s']['y'], 'c': [ line1, line2 ] }
  elif (
    line1['t'] == 'V' and
    line2['t'] == 'H' and
    line1['s']['y'] < line2['s']['y'] and
    line1['e']['y'] > line2['e']['y'] and
    line2['s']['x'] < line1['s']['x'] and
    line2['e']['x'] > line1['e']['x']
  ):
    return { 'x': line1['s']['x'], 'y': line2['s']['y'], 'c': [ line1, line2 ] }
  else:
    return None

def manhattan(point1, point2):
  return abs(point1['x'] - point2['x']) + abs(point1['y'] - point2['y'])

lines = [
  moves2lines(moves[0]),
  moves2lines(moves[1])
]

results = []

for line1 in lines[0]['H']:
  for line2 in lines[1]['V']:
    result = cross(line1, line2)
    if (result != None):
      results.append(result)

for line1 in lines[0]['V']:
  for line2 in lines[1]['H']:
    result = cross(line1, line2)
    if (result != None):
      results.append(result)

print "results = ", json.dumps(results, indent=4, sort_keys=True)

best = None

for result in results:
  current = manhattan(result, {'x': 0, 'y': 0})
  print current
  if (best == None or current < best):
    best = current
  
print best
