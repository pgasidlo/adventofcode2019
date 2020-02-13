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

  ops = []
  ip = 0

  def __init__(self, ops):
    self.ops = ops

  def run(self):

    loop = True

    while loop:
      intOp = IntOp(self.ops[self.ip])
      self.ip = self.ip + 1
      opcode = intOp.getOpcode()
      argCount = intOp.getArgCount()
      #print "opcode =", opcode, "argCount =", argCount

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

        args.append({
          'type': argType,
          'value': argValue,
        })

      if (opcode == IntOp.OP_HALT):
        loop = False
        break
      elif (opcode == IntOp.OP_ADD):
        self.ops[args[2]['value']] = args[0]['value'] + args[1]['value']
      elif (opcode == IntOp.OP_MUL):
        self.ops[args[2]['value']] = args[0]['value'] * args[1]['value']
      elif (opcode == IntOp.OP_IN):
        self.ops[args[0]['value']] = input("Input: ")
      elif (opcode == IntOp.OP_OUT):
        print "Output =", args[0]['value']
      elif (opcode == IntOp.OP_JMP_IF_TRUE):
        if (args[0]['value'] != 0):
          self.ip = args[1]['value']
      elif (opcode == IntOp.OP_JMP_IF_FALSE):
        if (args[0]['value'] == 0):
          self.ip = args[1]['value']
      elif (opcode == IntOp.OP_LESS_THAN):
        if (args[0]['value'] < args[1]['value']):
          self.ops[args[2]['value']] = 1
        else:
          self.ops[args[2]['value']] = 0
      elif (opcode == IntOp.OP_EQUALS):
        if (args[0]['value'] == args[1]['value']):
          self.ops[args[2]['value']] = 1
        else:
          self.ops[args[2]['value']] = 0


ops = open("input.txt", "r").readline().split(",");
ops = list(map(int, ops))

intMachine = IntMachine(ops)
intMachine.run()
