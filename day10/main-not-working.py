import copy
import sys
import fractions

# Rozmiar mapy asteroidow
ams = None
# Mapa asteroidow
am = []
# Wczytanie mapy
ar = 0
for aml in open("input5.txt"):
  aml = aml.rstrip()
  if (ams is None):
    ams = len(aml)
  am.append(aml)
  ar = ar + 1
  if (ar == ams):
    break

# Rozszerzenie mapy, przerobienie na liste list
am = map(list, [ ' ' * (3 * ams - 2) ] * (ams - 1) + map(lambda s: ' ' * (ams - 1) + s + ' ' * (ams - 1), am) + [ ' ' * (3 * ams - 2) ])

print "ams =", ams

def graph(am):
  for aml in am:
    print ''.join(aml)

def get(am, x, y):
  try:
    return am[y][x]
  except IndexError:
    return ' '

def put(am, x, y, char = ' '):
  try:
    am[y][x] = char
  except IndexError:
    pass

def distance(am, x, y):
  if (am[y][x] != '#'):
    return 0
  print "S: x =", x, "y =", y
  am = copy.deepcopy(am)
  put(am, x, y, 'X')
  for d in (range(1, ams, 1)):

    dds = []

    print "d =", d

    # Poziomo X+
    #print "x+"
    for xc in range(x - d, x + d):
      yc = y - d
      #print xc, yc
      if (get(am, xc, yc) == '#'):
        dds.append([ xc - x, yc - y ]);

    # Pionowo Y+
    #print "y+"
    for yc in range(y - d, y + d):
      xc = x + d
      #print xc, yc
      if (get(am, xc, yc) == '#'):
        dds.append([ xc - x, yc - y ]);

    # Poziomo X-
    #print "x-"
    for xc in range(x + d, x - d, -1):
      yc = y + d
      #print xc, yc
      if (get(am, xc, yc) == '#'):
        dds.append([ xc - x, yc - y ]);

    # Pionowo Y-
    #print "y-"
    for yc in range(y + d, y - d, -1):
      xc = x - d
      #print xc, yc
      if (get(am, xc, yc) == '#'):
        dds.append([ xc - x, yc - y ]);

    print "GO"
    for dd in dds:
      print "dd =", dd
      xd = x
      yd = y
      xd = xd + dd[0]
      yd = yd + dd[1]
      div = fractions.gcd(abs(dd[0]), abs(dd[1]))
      dd[0] = dd[0] / div
      dd[1] = dd[1] / div
      while (
          xd < x + ams and
          xd > 0 and
          yd < y + ams and
          yd > 0
       ):
        xd = xd + dd[0]
        yd = yd + dd[1]

        #print xd, yd

        if (get(am, xd, yd) == '#'):
          put(am, xd, yd, '+')
        else:
          put(am, xd, yd, ' ')

  graph(am)

  d = 0
  for x in range(0 + ams - 1, 2 * ams):
    for y in range(0 + ams - 1, 2 * ams):
      if (get(am, x, y) == '#'):
        d = d + 1

  return d

best = None
for x in range(ams):
  for y in range(ams):
    d = distance(am, x + (ams - 1), y + (ams - 1))
    print "x =", x, "y =", y, "distance =", d
    if (best is None or best['d'] < d):
      best = {'x': x, 'y': y, 'd': d}

print best

