ops = open("input.txt", "r").readline().split(",");

# https://stackoverflow.com/questions/10145347/convert-string-to-integer-using-map
# ops = [ int(x) for x in ops ]
ops = list(map(int, ops))

# ... before running the program, replace position 1 with the value 12 and replace position 2 with the value 2.
ops[1] = 12;
ops[2] = 2;

i = 0
while True:
    op = ops[i]
    print "i = ", i, "op = ", op
    i = i + 1
    if (op == 99):
        break;
    elif (op == 1 or op == 2):

        i1 = ops[i]
        v1 = ops[i1]
        i = i + 1
        i2 = ops[i]
        v2 = ops[i2]
        i = i + 1
        i3 = ops[i]
        i = i + 1

        if (op == 1):
            v3 = v1 + v2
        elif (op == 2):
            v3 = v1 * v2

        ops[i3] = v3

        print "ops[{}] = {} ops[{}] = {} ops[{}] = {}".format(i1, v1, i2, v2, i3, v3)

    else:
        raise Exception("invalid op: " + op)
print "ops[0] = ", ops[0]


