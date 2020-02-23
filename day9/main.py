import itertools
import sys

class IntOp:

  OP_HALT         = '99'
  OP_ADD          = '01'
  OP_MUL          = '02'
  OP_IN           = '03'
  OP_OUT          = '04'
  OP_JMP_IF_TRUE  = '05'
  OP_JMP_IF_FALSE = '06'
  OP_LESS_THAN    = '07'
  OP_EQUALS       = '08'
  OP_BASE         = '09'

  ARG_RELATIVE    = '2'
  ARG_IMMEDIATE   = '1'
  ARG_POSITION    = '0'

  DIR_INPUT       = 0
  DIR_OUTPUT      = 1

  ops = {
    OP_HALT: [],
    OP_ADD: [ DIR_INPUT, DIR_INPUT, DIR_OUTPUT ],
    OP_MUL: [ DIR_INPUT, DIR_INPUT, DIR_OUTPUT ],
    OP_IN:  [ DIR_OUTPUT ],
    OP_OUT: [ DIR_INPUT ],
    OP_JMP_IF_TRUE: [ DIR_INPUT, DIR_INPUT ],
    OP_JMP_IF_FALSE: [ DIR_INPUT, DIR_INPUT ],
    OP_LESS_THAN: [ DIR_INPUT, DIR_INPUT, DIR_OUTPUT ],
    OP_EQUALS: [ DIR_INPUT, DIR_INPUT, DIR_OUTPUT ],
    OP_BASE: [ DIR_INPUT ]
  }

  op = None

  def __init__(self, op):
    self.op = str(op).zfill(5)

  def getOpcode(self):
    return self.op[3:]

  def getArgCount(self):
    return len(self.ops[self.getOpcode()])

  def getArgType(self, arg):
    if (self.op[2 - arg] == '2'):
      return self.ARG_RELATIVE
    elif (self.op[2 - arg] == '1'):
      return self.ARG_IMMEDIATE
    else:
      return self.ARG_POSITION

  def getArgDir(self, arg):
    return self.ops[self.getOpcode()][arg]

class IntMachine:

  def __init__(self, ops):
    self.init = ops

  def resize(self, index):
    if (len(self.ops) <= index):
      delta = index - len(self.ops) + 1
      self.ops += [ 0 ] * delta
      # print "resize: delta =", delta, "len =", len(self.ops)

  def read(self, index):
    self.resize(index)
    return self.ops[index]

  def write(self, index, value):
    self.resize(index)
    self.ops[index] = value

  def reset(self, stdin = []):
    self.base = 0
    self.ops = list(self.init)
    self.ip = 0
    self.done = False
    self.stdin = stdin
    return self

  def run(self, stdin1 = []):

    stdout = []
    self.stdin.extend(stdin1)

    loop = True

    while loop:
      origIp = self.ip
      intOp = IntOp(self.read(self.ip))
      self.ip = self.ip + 1
      opcode = intOp.getOpcode()
      argCount = intOp.getArgCount()

      argsRaw = []
      args = []
      for argIndex in range(0, argCount):
        argValue = self.read(self.ip)
        self.ip = self.ip + 1
        argsRaw.append(argValue)
        argType = intOp.getArgType(argIndex)
        argDir = intOp.getArgDir(argIndex)
        if (argDir == IntOp.DIR_INPUT):
          if (argType == IntOp.ARG_POSITION):
            argValue = self.read(argValue)
          elif (argType == IntOp.ARG_RELATIVE):
            argValue = self.read(argValue + self.base)
        else:
          if (argType == IntOp.ARG_RELATIVE):
            argValue = argValue + self.base

        args.append(argValue)

      # print "ops =", self.ops
      # print "pos =", origIp, "base =", self.base, "opcodeRaw =", intOp.op, "opcode =", opcode, "argCount =", argCount, "argsRaw =", argsRaw, "args =", args

      if (opcode == IntOp.OP_HALT):
        self.done = True
        return stdout
      elif (opcode == IntOp.OP_ADD):
        self.write(args[2], args[0] + args[1])
      elif (opcode == IntOp.OP_MUL):
        self.write(args[2], args[0] * args[1])
      elif (opcode == IntOp.OP_IN):
        try:
          value = self.stdin.pop(0)
        except IndexError:
          self.ip = origIp
          return stdout
        self.write(args[0], value)
        # print "input =", value
      elif (opcode == IntOp.OP_OUT):
        stdout.append(args[0])
        # print "output =", stdout
      elif (opcode == IntOp.OP_JMP_IF_TRUE):
        if (args[0] != 0):
          self.ip = args[1]
      elif (opcode == IntOp.OP_JMP_IF_FALSE):
        if (args[0] == 0):
          self.ip = args[1]
      elif (opcode == IntOp.OP_LESS_THAN):
        if (args[0] < args[1]):
          self.write(args[2], 1)
        else:
          self.write(args[2], 0)
      elif (opcode == IntOp.OP_EQUALS):
        if (args[0] == args[1]):
          self.write(args[2], 1)
        else:
          self.write(args[2], 0)
      elif (opcode == IntOp.OP_BASE):
        self.base = self.base + args[0]
    return stdout

init = list(map(int, open("input.txt").read().split(",")))

m = IntMachine(init)

print "part1"
print m.reset().run([ 1 ])
print "part2"
print m.reset().run([ 2 ])
