import sys
import copy
from fractions import gcd
from numpy import arctan
import math

import pprint
pp = pprint.PrettyPrinter(indent=4)

am = []
ams = None
for aml in open("input.txt"):
  aml = aml.rstrip()
  if (ams is None):
    ams = len(aml)
  am.append(list(aml))

def graph(am):
  for aml in am:
    print "".join(aml)

def calculate(am, x, y):
  if (am[y][x] != '#'):
    return {}
  am = copy.deepcopy(am)
  am[y][x] = 'X';

  r = {}

  for cx in range(ams):
    for cy in range(ams):
      if (am[cy][cx] == '#'):
        dx = cx - x
        dy = cy - y
        g = gcd(abs(dx),abs(dy))
        # print 'x = {} -> {} = {}, y = {} -> {} = {}, g = {}'.format(x,cx,dx,y,cy,dy,g)
        dx = dx / g
        dy = dy / g

        if (dy == 0):
          if (dx < 0):
            fi = 270.00
          else:
            fi = 90.00
        elif (dx == 0):
          if (dy < 0):
            fi = 0.00
          else:
            fi = 180.00
        else:
          fi = arctan(1.0 * dx/dy) * 180.0 / math.pi
          if (dx < 0):
            if (dy < 0):
              fi = 360.00 - fi
              pass
            else:
              fi = 180.00 - fi
              pass
          else:
            if (dy < 0):
              fi = -fi
              pass
            else:
              fi = 180.00 - fi
              pass

        d = math.sqrt(cx * cx + cy * cy)
        key = '{}|{}'.format(dx,dy)
        if not key in r:
          r[key] = { 'fi': fi, 'dx': dx, 'dy': dy, 'as': [] }
        r[key]['as'].append({'x': cx, 'y': cy, 'd': d});

  return r

best = None

for x in range(ams):
  for y in range(ams):
    r = calculate(am, x, y)
    c = len(r.keys())
    # print 'x = {}, y = {}, c = {}'.format(x,y,c)
    if (best is None or best['c'] < c):
      best = { 'x': x, 'y': y, 'c': c, 'r': r }

#pp.pprint(best)

print "part1 = ", best['c']

def vaporize(am, best):

  r = best['r'].values()
  r.sort(key=lambda v:v['fi'])

  for v in r:
    v['as'].sort(key=lambda v:v['d'], reverse=True)

  # pp.pprint(r)

  fis = map(lambda v:v['fi'], r)

  c = 0
  i = 0
  n = len(r)
  while True:
    if (len(r[i]['as'])):
      a = r[i]['as'].pop(0)
      c = c + 1
      if (c == 200):
        print "part2: c =", c, "x =", a['x'], "y =", a['y']
      f = True
    i = i + 1
    if (i == n):
      if (not f):
        break
      i = 0
      f = False

vaporize(am, best)
