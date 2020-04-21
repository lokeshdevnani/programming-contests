
Global_DV = ['W', 'E', 'N', 'S']
NUM = 10**9

def apply_direction(DV, direction):
  idx = index_DV(direction)
  DV[idx]+=1

def multiply_direction(DV, times):
  for i in range(0, 4):
    DV[i] *= times

def add_DV(DV, dv2):
  for i in range(0, 4):
    DV[i] += dv2[i]

def to_DV(direction):
  dv = [0, 0, 0, 0]
  apply_direction(dv, direction)
  return dv

def index_DV(direction):
  return Global_DV.index(direction)

def is_DV(element):
  return type(element) is list

def expression_to_dv(expression):
  multiplier_stack = []
  operator_stack = []

  N = len(expression)
  for i in range(0, N):
    ch = expression[i]

    if ch.isalpha():
      if len(operator_stack) > 0 and is_DV(operator_stack[-1]):
        apply_direction(operator_stack[-1], ch)
      else:
        operator_stack.append(to_DV(ch))

    if ch == '(':
      operator_stack.append(ch)

    if ch.isdigit():
      multiplier_stack.append(int(ch))

    if ch == ')':
      dv2 = operator_stack.pop()
      operator_stack.pop() # remove (
      coefficient = multiplier_stack.pop()
      multiply_direction(dv2, coefficient)
      if len(operator_stack) > 0 and is_DV(operator_stack[-1]):
        add_DV(operator_stack[-1], dv2)
      else:
        operator_stack.append(dv2)

  while len(multiplier_stack) > 0:
    dv2 = operator_stack.pop()
    operator_stack.pop() # remove (
    coefficient = multiplier_stack.pop()
    multiply_direction(dv2, coefficient)
    operator_stack.append(dv2)

  return operator_stack[-1]

def expression_to_coordinates(expression):
  dv = expression_to_dv(expression)
  return [(NUM + dv[1] - dv[0]) % NUM + 1, (NUM + dv[3] - dv[2]) % NUM + 1]

t = int(input())
for i in range(1, t + 1):
  expression = input()
  coordinates = expression_to_coordinates(expression)
  print("Case #{}: {} {}".format(i, coordinates[0], coordinates[1]))


