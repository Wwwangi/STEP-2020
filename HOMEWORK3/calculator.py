def read_number(line, index, neg):
  number = 0
  #Deal with integer part
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  #Deal with decimal part
  if index < len(line) and line[index] == '.':
    index += 1
    keta = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * keta
      keta /= 10
      index += 1
  if neg == True:
    number *= -1
    neg = False
  token = {'type': 'NUMBER', 'number': number}
  return token, index, neg

def read_operator(line,index):
  operator=line[index]
  if(operator=='+'):
    token = {'type': '+'}
  elif(operator=='-'):
    token = {'type': '-'}
  elif(operator=='*'):
    token = {'type': '*'}
  elif(operator=='/'):
    token = {'type': '/'}
  elif(operator=='('):
    token = {'type': '('}
  elif(operator==')'):
    token = {'type': ')'}
  return token, index + 1

#Tokenize the string into numbers and operators
def tokenize(line):
  tokens = []
  index = 0
  neg = False
  prev = ''
  while index < len(line):
    if line[index].isdigit():
      (token, index, neg) = read_number(line, index, neg)
      prev = 'number'
    elif line[index] == '-' and (prev == '' or prev in set(['+','-','*','/','('])):
      neg = True
      index += 1
      continue
    elif line[index] in set(['+','-','*','/','(',')']):
      prev = line[index]
      (token, index) = read_operator(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens

#Change a infix expression to the suffix expression for later calculation
def Infix_To_Suffix_Expression(tokens):
  #Record the operation priority i.e. '()' > */' > '+-'
  Priority={'+':0,'-':0,'*':1,'/':1,'(':2,')':2}
  #a stack that stores the operators
  operator_stack=[]
  #a list that stores the suffix expression
  tokens_suffix=[]
  index=0
  while index<len(tokens):
    Type=tokens[index]['type']
    #if the token is a number, directly append it to the final suffix expression list
    if(Type=='NUMBER'):
      tokens_suffix.append(tokens[index]['number'])
      index+=1
    #if the token is a operator
    else:
      #if the priority of current operator is greater than the priority of the last operator stored in the stack, then directly append it to the operator stack 
      if not operator_stack or (Type!=')' and Priority[Type]>Priority[operator_stack[-1]]):
        operator_stack.append(Type)
      #if the operator is a right parenthesis, append all the operators in the operator stack to the suffix expression until a left parenthsis is found
      elif(Type==')'):
        while operator_stack[-1]!='(':
          operator=operator_stack.pop()
          tokens_suffix.append(operator)
        #Remove the left parenthsis in the operator stack
        operator_stack.pop()          
      else:
        #append all the operators that have higher priority than that of the current operator to the suffix expression list 
        while operator_stack and operator_stack[-1]!='(' and Priority[Type]<=Priority[operator_stack[-1]]:
          operator=operator_stack.pop()
          tokens_suffix.append(operator)
        #Append the current operator to the operator list
        operator_stack.append(Type)
      index+=1
  #Append remaining operators in the operator stack to the suffix expression
  while operator_stack:
    tokens_suffix.append(operator_stack.pop())
  return tokens_suffix

#Calculate using suffix expression
def evaluate(tokens):
  tokens=Infix_To_Suffix_Expression(tokens)
  answer_stack=[]
  operators=set(['+','-','*','/'])
  for token in tokens:
    #if token is a number, directly append it to the answer_stack
    if token not in operators:
      answer_stack.append(token)
    #if token is an operator, pop the previous two elements in answer_stack to do +-*/ operations, then append the result back to the answer_stack
    else:
      try:
        temp1=answer_stack.pop()
        temp2=answer_stack.pop()
        if(token=='+'):
          answer_stack.append(temp1+temp2)
        elif(token=='-'):
          answer_stack.append(temp2-temp1)
        elif(token=='*'):
          answer_stack.append(temp1*temp2)
        elif(token=='/'):
          answer_stack.append(temp2/temp1)
      except:
        print('Invalid Syntax')
        exit(1)
  return answer_stack[0]

def test(line):
  tokens = tokenize(line)
  actual_answer = evaluate(tokens)
  expected_answer = eval(line)
  if abs(actual_answer - expected_answer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expected_answer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actual_answer))

#Some test cases
def runTest():
  print("==== Test started! ====")
  test('1')
  test('11')
  test('11.1')
  test('2+3')
  test('2-3')
  test('2*3')
  test('2/3')
  test('2+3.0')
  test('2-3.0')
  test('2*3.0')
  test('2/3.0')
  test('2+3+4')
  test('2-3-4')
  test('2+3*4')
  test('2*3+4')
  test('2-3/4')
  test('2/3-4')
  test('2*3.0+4/5.0')
  test('2*3.0-4/5.0')
  test('2*3*4*5')
  test('2/3/4/5')
  test('(1)')
  # Redundant nested parenthses
  test('((1))')
  test('((2+3))')
  test('((2+3)-4)')
  test('1-(2-3)')
  test('1-(2-(3-4))')
  test('1-(2-(3-(4-5)))')
  test('1-(2-(3-(4-5)-6))')
  test('1-(2-(3-(4-5)-6)-7)')
  test('1-(2-(3-(4-5)-6)-7)-8')
  test('(1+2)*3')
  test('1*(2+3)')
  test('(1-2)/3')
  test('1/(2-3)')
  test('(1+2)*(3+4)')
  test('((1+2)*(3+4))*((1+2)*(3+4))')
  # Negative numbers
  test('-1')
  test('-11')
  test('-11.1')
  test('-2+3')
  test('-2-3')
  test('-2*3')
  test('2/(-3)')
  test('-2+3.0')
  test('-2-3.0')
  test('-2*3.0')
  test('2/(-3.0)')
  test('2+3+(-4)')
  test('2-3-(-4)')
  test('2+3*(-4)')
  test('2*(-3)+4')
  test('2-3/(-4)')
  test('2/(-3)-4')
  test('2*(-3.0)+4/5.0')
  test('2*3.0-4/(-5.0)')
  test('2*3*(-4)*5')
  test('2/(-3)/4/5')
  print("==== Test finished! ====\n")

runTest()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)