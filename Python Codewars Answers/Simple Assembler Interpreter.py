def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def parse_instruction(instruction):
  return instruction.split(' ')
  
class Program:
  def __init__(self, program):
    self.registers = {}
    self.line = 0
    self.program = program
    self.commands  = {'mov': self.execute_mov, 'inc': self.execute_inc, 'dec': self.execute_dec, 'jnz': self.execute_jnz}
    
  def execute_mov(self, *params):
    [destination, origin] = params
    if is_number(origin):
      self.registers[destination] = int(float(origin))
    else:
      self.registers[destination] = self.registers[origin]
    
  def execute_inc(self, *params):
    [register] = params
    self.registers[register] = self.registers[register] + 1

  def execute_dec(self, *params):
    [register] = params
    self.registers[register] = self.registers[register] - 1
  
  def execute_jnz(self, *params):
    [flag, inc] = params
    if is_number(flag):
      is_zero = int(float(flag)) == 0
    else:
      is_zero = self.registers[flag] == 0
    if not is_zero:
      self.line = self.line + int(float(inc)) - 1

  def execute(self):
    instructions = [parse_instruction(instruction) for instruction in self.program]
    while self.line < len(instructions):
      instruction = instructions[self.line]
      self.commands[instruction[0]](*instruction[1:])
      self.line = self.line + 1 
    return self.registers
    
def simple_assembler(program):
  return Program(program).execute()
