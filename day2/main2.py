import copy

# With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to determine what pair of inputs produces the output 19690720.
expected = 19690720

debug = 1

ops_base = list(map(int, open("input.txt", "r").readline().split(",")));

class IntCode:

    debug = 0

    def __init__(self, ops):
        self.ops = ops

    def run(self, noun, verb):
        ops = copy.copy(self.ops)
        ops[1] = noun
        ops[2] = verb
        i = 0
        while True:
            op = ops[i]
            if self.debug:
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

                if self.debug:
                    print "ops[{}] = {} ops[{}] = {} ops[{}] = {}".format(i1, v1, i2, v2, i3, v3)

            else:
                raise Exception("invalid op: " + op)
        return ops[0]

intcode = IntCode(ops_base)
intcode.debug = debug

found = 0
for noun in range(0, 100):
    for verb in range(0, 100):
        try:
            result = intcode.run(noun, verb)
            if debug:
                print "noun = ", noun, "verb = ", verb, "result = ", result
            if (result == expected):
                found = 1
                break
        except:
            if debug:
                print "noun = ", noun, "verb = ", verb, "exception"
    if (found == 1):
        break

if found:
    print "result = ", noun * 100 + verb
else:
    print "not found"

