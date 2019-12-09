import re
table=[]
expression=input().split(' ')
print(expression)
#expression=['a','b','c','+','+']
stack=[]
i=0
list=[]
operators=['+','-','*','/']
for ch in expression:
  if ch in operators:
    second=stack.pop()
    first=stack.pop()
    temp="t"+str(i+1)+"="+str(first)+str(ch)+str(second)
    list.append(temp)
    print(temp)
    stack.append("t"+str(i+1))
    i=i+1
  else:
    stack.append(ch)
print(list)

for expr in list:
  term=re.split('\=|\+|\-|\/|\*',expr)
  print(term)
  row=[]
  
  if '+' in expr :
    row.append('+')
  elif '-' in expr :
    row.append('-')
  elif '*' in expr :
    row.append('*')
  elif '/' in expr :
    row.append('/')
  row.append(term[1])
  row.append(term[2])
  row.append(term[0])
  table.append(row)
print("operator   operand1   opreand2   result")
for row in table :
    for item in row:
        print("       "+item+" ",end="")
    print(" ")
#print(table)

# ['b', 'b', '*', '44', '-', 'a', '*', 'c', '*']
# t1=b*b
# t2=t1-44
# t3=t2*a
# t4=t3*c
# ['t1=b*b', 't2=t1-44', 't3=t2*a', 't4=t3*c']
# ['t1', 'b', 'b']
# ['t2', 't1', '44']
# ['t3', 't2', 'a']
# ['t4', 't3', 'c']
# operator   operand1   opreand2   result
#       *        b        b        t1  
#       -        t1        44        t2  
#       *        t2        a        t3  
#       *        t3        c        t4