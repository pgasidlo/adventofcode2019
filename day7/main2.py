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

  ARG_IMMEDIATE = 1
  ARG_POSITION = 0

  ops = {
    OP_HALT: {
      'args': []
    },
    OP_ADD: {
      'args': [
        None,
        None,
        ARG_IMMEDIATE
      ]
    },
    OP_MUL: {
      'args': [
        None,
        None,
        ARG_IMMEDIATE
      ]
    },
    OP_IN: {
      'args': [
        ARG_IMMEDIATE
      ]
    },
    OP_OUT: {
      'args': [
        None
      ]
    },
    OP_JMP_IF_TRUE: {
      'args': [
        None,
        None
      ]
    },
    OP_JMP_IF_FALSE: {
      'args': [
        None,
        None
      ]
    },
    OP_LESS_THAN: {
      'args': [
        None,
        None,
        ARG_IMMEDIATE
      ]
    },
    OP_EQUALS: {
      'args': [
        None,
        None,
        ARG_IMMEDIATE
      ]
    },
  }

  op = None

  def __init__(self, op):
    self.op = str(op).zfill(5)

  def getOpcode(self):
    return self.op[3:]

  def getArgCount(self):
    return len(self.ops[self.getOpcode()]['args'])

  def getArgType(self, arg):
    args = self.ops[self.getOpcode()]['args']
    if (args[arg] == None):
      if (self.op[2 - arg] == '1'):
        return self.ARG_IMMEDIATE
      else:
        return self.ARG_POSITION
    else:
      return args[arg]

class IntMachine:

  def __init__(self, ops):
    self.init = ops

  def reset(self, stdin = []):
    self.ops = list(self.init)
    self.ip = 0
    self.done = False
    self.stdout = []
    self.stdin = stdin
    return self

  def run(self, stdin1 = []):

    self.stdin.extend(stdin1)

    loop = True

    while loop:
      origIp = self.ip

      intOp = IntOp(self.ops[self.ip])
      self.ip = self.ip + 1
      opcode = intOp.getOpcode()
      argCount = intOp.getArgCount()

      args = []
      for argIndex in range(0, argCount):
        #print "argIndex =", argIndex
        argValue = self.ops[self.ip]
        argImmediate = argValue
        #print "argValue =", argValue
        self.ip = self.ip + 1
        argType = intOp.getArgType(argIndex)
        if (argType == IntOp.ARG_POSITION):
          argValue = self.ops[argValue]

        args.append(argValue);

      # print "pos =", origIp, "opcode =", opcode, "argCount =", argCount, "args =", args

      if (opcode == IntOp.OP_HALT):
        self.done = True
        return self.stdout
      elif (opcode == IntOp.OP_ADD):
        self.ops[args[2]] = args[0] + args[1]
      elif (opcode == IntOp.OP_MUL):
        self.ops[args[2]] = args[0] * args[1]
      elif (opcode == IntOp.OP_IN):
        try:
          value = self.stdin.pop(0)
        except IndexError:
          self.ip = origIp
          return self.stdout
        self.ops[args[0]] = value
        # print "input =", value
      elif (opcode == IntOp.OP_OUT):
        self.stdout = args[0]
        # print "output =", self.stdout
      elif (opcode == IntOp.OP_JMP_IF_TRUE):
        if (args[0] != 0):
          self.ip = args[1]
      elif (opcode == IntOp.OP_JMP_IF_FALSE):
        if (args[0] == 0):
          self.ip = args[1]
      elif (opcode == IntOp.OP_LESS_THAN):
        if (args[0] < args[1]):
          self.ops[args[2]] = 1
        else:
          self.ops[args[2]] = 0
      elif (opcode == IntOp.OP_EQUALS):
        if (args[0] == args[1]):
          self.ops[args[2]] = 1
        else:
          self.ops[args[2]] = 0
    return self.stdout

init = list(map(int, open("input.txt").read().split(",")))

permutations = list(itertools.permutations(range(5, 10)));

best = {
  'permutation': None,
  's': 0
}

for permutation in permutations:

  # print "## permutation = ", permutation

  intMachines = [
      IntMachine(init).reset([permutation[0]]),
      IntMachine(init).reset([permutation[1]]),
      IntMachine(init).reset([permutation[2]]),
      IntMachine(init).reset([permutation[3]]),
      IntMachine(init).reset([permutation[4]]),
  ]

  s = 0
  complete = False
  amp = 0
  while not complete:
    for amp in range(5):
      # print "### amp =", amp, "signal =", s
      intMachine = intMachines[amp]
      s = intMachine.run([ s ])
      complete = intMachine.done

  if (s > best['s']):
    best['permutation'] = permutation;
    best['s'] = s

print best
