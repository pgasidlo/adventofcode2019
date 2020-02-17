import sys

class Tree:
    value = None
    parent = None
    children = None

    def __init__(self, value):
        self.value = value
        self.children = []

    def appendTree(self, tree):
        tree.parent = self
        self.children.append(tree)
        return self

    def appendValue(self, value):
        child = Tree(value)
        child.parent = self
        self.children.append(child)
        return self

    def graph(self, indent = 0):
        spacer = "\t".expandtabs(1) * indent
        print spacer, self.value
        for child in self.children:
            child.graph(indent + 1)

    def find(self, value):
        if (self.value == value):
            return self
        else:
            for child in self.children:
                result = child.find(value)
                if (result != None):
                    return result
            return None

    def orbits(self, depth = 0):

        sum = depth

        for child in self.children:
            sum = sum + child.orbits(depth + 1)
        return sum

trees = []

for line in open("input.txt"):
    points = line.rstrip().split(')')
    # print "parent =", points[0], "child =", points[1]
    if (len(trees) == 0):
        trees.append(Tree(points[0]).appendValue(points[1]))
    else:
        n = len(trees)
        fi = False
        for i in range(n):
            if (trees[i] == None):
                continue
            child = trees[i].find(points[0]);
            if (child):
                fi = True
                fj = False
                for j in range(n):
                    if (i == j):
                        continue
                    if (trees[j].value == points[1]):
                        child.appendTree(trees[j])
                        trees[j] = None
                        fj = True
                        break
                if (not fj):
                    child.appendValue(points[1])
                break
        if (not fi):
            fj = False
            for j in range(n):
                if (trees[j].value == points[1]):
                    trees.append(Tree(points[0]).appendTree(trees[j]))
                    trees[j] = None
                    fj = True
                    break
            if (not fj):
                trees.append(Tree(points[0]).appendValue(points[1]))

    trees = list(filter(lambda x: x != None, trees))

print "orbits = ", trees[0].orbits()
