children = {}

for line in open("input.txt"):
    points = line.rstrip().split(')')
    if points[0] not in children:
        children[points[0]] = { 'children': [], 'depth': None, 'path': [] }
    if points[1] not in children:
        children[points[1]] = { 'children': [], 'depth': None, 'path': [] }
    children[points[0]]['children'].append(points[1])

def depthme(i, depth, path = None):
    global children
    children[i]['depth'] = depth
    if (path):
        path = path + "-" + i
        children[i]['path'] = path
    else:
        path = i
    for j in children[i]['children']:
        depthme(j, depth + 1, path)

depthme('COM', 0)

sum = 0
for key in children:
    sum = sum + children[key]['depth']

print "sum =", sum

pa = children['SAN']['path'].split("-")
pb = children['YOU']['path'].split("-");
la = len(pa)
lb = len(pb)

n = min(la, lb)

lc = 0
for i in range(n):
    ai = pa[i]
    bi = pb[i]
    if (ai != bi):
        lc = i - 1
        break


print "transfers =", la - lc - 2 + lb - lc - 2
