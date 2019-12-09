
# First and Follow
import re

no_of_rules = int(input("Enter the number of rules : "))
list_of_rules = []
i = 0
while i < no_of_rules:
    list_of_rules.append(input("Rule " + str(i + 1) + " : "))
    i = i + 1

print(list_of_rules)
old_rules = []
rule_status = []
rule_id = []
first_list = []
i = 0
while i < no_of_rules:
    old_rules.append(re.split('->|\|', list_of_rules[i]))
    rule_status.append(False)
    rule_id.append(old_rules[i][0].strip())
    i = i + 1
print(old_rules)
# Rule 1 and Rule 2
i = 0
while i < len(old_rules):
    j = 1
    temp_list = []
    value = True
    while j < len(old_rules[i]):
        temp = old_rules[i][j].strip()
        if temp != "abs" and not temp[0].islower():
            value = False
            break
        j += 1
    rule_status[i] = value
    j = 1
    while j < len(old_rules[i]):
        temp = old_rules[i][j].strip()
        if temp == "abs":
            temp_list.append(temp)
        elif temp[0].islower() or temp.islower():
            temp_list.append(temp[0])
        j += 1
    first_list.append(temp_list)
    i += 1
print(rule_status)
print(rule_id)
print(first_list)
print("----------------------------------------------------------------------")

while False in rule_status:
    i = 0
    while i < len(old_rules):
        if (rule_status[i] == True):
            i = i + 1
            continue
        j = 1
        temp_status = [False] * (len(old_rules[i]) - 1)
        m = 1
        while m < (len(old_rules[i])):
            if old_rules[i][m].strip() == "abs" or (old_rules[i][m].strip())[0].islower():
                temp_status[m - 1] = True
            m += 1

        while j < len(old_rules[i]):
            if old_rules[i][j].strip() == "abs" or (old_rules[i][j].strip())[0].islower():
                j += 1
                continue
            temp = old_rules[i][j].strip()

            y = [False] * len(temp)
            k = 0
            for a in temp:
                if a.islower() or rule_status[rule_id.index(a)]:
                    y[k] = True
                k += 1

            if False in y:
                break
            else:
                for a in temp:

                    if not a.islower() and not "abs" in first_list[rule_id.index(a)]:
                        first_list[i] = list(set(first_list[i] + first_list[rule_id.index(a)]))
                        break
                    elif not a.islower() and "abs" in first_list[rule_id.index(a)] and temp[-1] != a:
                        temp1 = list(first_list[rule_id.index(a)])
                        temp1.remove("abs")
                        first_list[i] = list(set(first_list[i] + temp1))

                    elif not a.islower() and "abs" in first_list[rule_id.index(a)] and temp[-1] == a:
                        temp1 = list(first_list[rule_id.index(a)])
                        first_list[i] = list(set(first_list[i] + temp1))
                    elif a.islower():
                        if not a in first_list[i]:
                            first_list[i].append(a)
                        break
                    else:
                        None
                print(first_list)
                temp_status[j - 1] = True
            j += 1
        if not False in temp_status:
            rule_status[i] = True
        i += 1

print("First : ")
print(first_list)
print("Follow :")
start = input("Enter the start symbol : ")
follow_list = []

i = 0
while i < no_of_rules:
    temp_list = []
    if old_rules[i][0] == start:
        temp_list.append("$")
    follow_list.append(temp_list)
    i += 1
print(follow_list)
i = 0
while i < no_of_rules:
    character = old_rules[i][0]
    j = 0
    while j < no_of_rules:
        temp = ''.join(old_rules[j][1:])
        if not character in temp:
            j = j + 1
            continue
        follow = []
        list_contain_char = []
        for word in old_rules[j][1:]:
            if character in word:
                list_contain_char.append(word)
        for word in list_contain_char:
            start_index = word.index(character) + 1

            while start_index < len(word):
                if word[start_index].islower():
                    if not word[start_index] in follow:
                        follow.append(word[start_index])
                    break
                elif start_index != (len(word) - 1) and not "abs" in first_list[rule_id.index(word[start_index])]:
                    follow = list(set(follow + first_list[rule_id.index(word[start_index])]))
                    break
                elif start_index != (len(word) - 1) and "abs" in first_list[rule_id.index(word[start_index])]:
                    temp1 = list(first_list[rule_id.index(word[start_index])])
                    temp1.remove("abs")
                    follow = list(set(follow + temp1))
                elif start_index == (len(word) - 1) and not "abs" in first_list[rule_id.index(word[start_index])]:
                    follow = list(set(follow + first_list[rule_id.index(word[start_index])]))
                    break
                elif start_index == (len(word) - 1) and "abs" in first_list[rule_id.index(word[start_index])]:
                    temp1 = list(first_list[rule_id.index(word[start_index])])
                    temp1.remove("abs")
                    follow = list(set(follow + temp1 + follow_list[j]))

                start_index += 1
            if start_index == (len(word)):
                follow = list(set(follow + follow_list[j]))
            follow_list[i] = list(set(follow_list[i] + follow))
        j += 1
    i += 1
print(follow_list)
print("----------------------------------PARSING TABLE--------------------------------------------------------")
print("Firstc :  ",first_list)
print('Follow :  ',follow_list)
terminal_list=[]
non_terminal_list=[]
i=0
while i<len(first_list):
    non_terminal_list.append((old_rules[i][0])[0])
    i+=1
k=0
while k<len(old_rules):
    m=1
    while m<len(old_rules[k]):
        temp=old_rules[k][m].strip()
        if temp =="abs":
            m+=1
            continue
        else :
            for a in temp:
                if a.islower() and not a in terminal_list:
                     terminal_list.append(a)
        m+=1
    k+=1
terminal_list.append("$")
print("Terminal List : ",terminal_list)
print("Non Terminal list : ",non_terminal_list)
table=[]
i=0
print("      ",terminal_list)
while i<len(old_rules):
    row=[]
    row.append(non_terminal_list[i])
    for k in range(len(terminal_list)):
        row.append([])
    character=(old_rules[i][0])[0]
    j=1
    while j<len(old_rules[i]):
        temp=old_rules[i][j]
        first_of_element=[]
        if temp =="abs":
            for b in follow_list[i]:
                temp1 = list( row[terminal_list.index(b) + 1])
                temp2=[]
                temp2.append(character + str("->abs"))
                row[terminal_list.index(b) + 1]=list(set(temp1+temp2))
                #row[terminal_list.index(b) + 1].append(character + str("->abs") )
            j+=1
            continue
            #first_of_element.append("abs")
        else :
            for a in temp:
                if not a.islower() and not "abs" in first_list[rule_id.index(a)]:
                    first_of_element = list(set(first_of_element + first_list[rule_id.index(a)]))

                    break
                elif not a.islower() and "abs" in first_list[rule_id.index(a)] and temp[-1] != a:
                    temp1 = list(first_list[rule_id.index(a)])
                    temp1.remove("abs")
                    first_of_element= list(set(first_of_element + temp1))


                elif not a.islower() and "abs" in first_list[rule_id.index(a)] and temp[-1] == a:
                    temp1 = list(first_list[rule_id.index(a)])
                    first_of_element = list(set(first_of_element+ temp1))

                elif a.islower():
                    if not a in first_of_element:
                        first_of_element.append(a)

                    break
                else:
                    None

        for a in first_of_element:
            if a =='abs':
                for b in follow_list[i]:
                    temp1 = list(row[terminal_list.index(b) + 1])
                    temp2 =[]
                    temp2.append(character + str("->")+temp )
                    row[terminal_list.index(b) + 1] = list(set(temp1+temp2))
                    #row[terminal_list.index(b) + 1].append(character + str("->")+temp )
            else:
                temp1 = list(row[terminal_list.index(a) + 1])
                temp2 = []
                temp2.append(character + str("->") + temp)
                row[terminal_list.index(a) + 1] = list(set(temp1 + temp2))

                #row[terminal_list.index(a)+1].append(character+str("->")+ temp)

        j+=1


    table.append(row)

    i+=1

for row in table:
    print(row)

for row in table:
    for element in row:
        if len(element)>=2:
            print("LL(1) is not possible")
            exit()

print("LL(1) is possible")
string=input("Enter the input string : ")
stack1=[]
stack1+="$"
stack1=[start]+stack1
input=[]
input.append("$")
for char in string:
    input=[str(char)]+input
run=True
print("       Stack       ,      Input         ")
print(stack1,input)
while run:
    symbol1 = stack1[0]
    symbol2 = input[0]
    if symbol1.strip().isupper():
        rule = table[rule_id.index(symbol1.strip())][terminal_list.index(symbol2.strip()) + 1]
        rule_new = re.split('->', rule[0])
        print(rule_new)
        stack1.pop(0)
        if rule_new[1] !="abs":
            for char in "".join(reversed(rule_new[1])):
                stack1 = [char] + stack1
        print(stack1, input)
        continue

    if stack1[0]=="$" and input[0]=="$":
        print(stack1,input)
        break
    if stack1[0]==input[0] and stack1[0].islower() :
        stack1.pop(0)
        input.pop(0)
        print(stack1, input)
    if stack1[0] != input[0] and stack1[0].islower() and input[0].islower():
        print("Input string not staisfied")



# "C:\Users\Austrin Dabre\PycharmProjects\ll1\venv\Scripts\python.exe" "C:/Users/Austrin Dabre/PycharmProjects/ll1/venv/ll1.py"
# Enter the number of rules : 5
# Rule 1 : E->TA
# Rule 2 : A->pTA|abs
# Rule 3 : T->FB
# Rule 4 : B->mFB|abs
# Rule 5 : F->oEc|i
# ['E->TA', 'A->pTA|abs', 'T->FB', 'B->mFB|abs', 'F->oEc|i']
# [['E', 'TA'], ['A', 'pTA', 'abs'], ['T', 'FB'], ['B', 'mFB', 'abs'], ['F', 'oEc', 'i']]
# [False, True, False, True, True]
# ['E', 'A', 'T', 'B', 'F']
# [[], ['p', 'abs'], [], ['m', 'abs'], ['o', 'i']]
# ----------------------------------------------------------------------
# [[], ['p', 'abs'], ['i', 'o'], ['m', 'abs'], ['o', 'i']]
# [['i', 'o'], ['p', 'abs'], ['i', 'o'], ['m', 'abs'], ['o', 'i']]
# First :
# [['i', 'o'], ['p', 'abs'], ['i', 'o'], ['m', 'abs'], ['o', 'i']]
# Follow :
# Enter the start symbol : E
# [['$'], [], [], [], []]
# [['c', '$'], ['c', '$'], ['c', 'p', '$'], ['c', 'p', '$'], ['c', 'p', 'm', '$']]
# ----------------------------------PARSING TABLE--------------------------------------------------------
# Firstc :   [['i', 'o'], ['p', 'abs'], ['i', 'o'], ['m', 'abs'], ['o', 'i']]
# Follow :   [['c', '$'], ['c', '$'], ['c', 'p', '$'], ['c', 'p', '$'], ['c', 'p', 'm', '$']]
# Terminal List :  ['p', 'm', 'o', 'c', 'i', '$']
# Non Terminal list :  ['E', 'A', 'T', 'B', 'F']
#        ['p', 'm', 'o', 'c', 'i', '$']
# ['E', [], [], ['E->TA'], [], ['E->TA'], []]
# ['A', ['A->pTA'], [], [], ['A->abs'], [], ['A->abs']]
# ['T', [], [], ['T->FB'], [], ['T->FB'], []]
# ['B', ['B->abs'], ['B->mFB'], [], ['B->abs'], [], ['B->abs']]
# ['F', [], [], ['F->oEc'], [], ['F->i'], []]
# LL(1) is possible
# Enter the input string : ipi
#        Stack       ,      Input
# ['E', '$'] ['i', 'p', 'i', '$']
# ['E', 'TA']
# ['T', 'A', '$'] ['i', 'p', 'i', '$']
# ['T', 'FB']
# ['F', 'B', 'A', '$'] ['i', 'p', 'i', '$']
# ['F', 'i']
# ['i', 'B', 'A', '$'] ['i', 'p', 'i', '$']
# ['B', 'A', '$'] ['p', 'i', '$']
# ['B', 'abs']
# ['A', '$'] ['p', 'i', '$']
# ['A', 'pTA']
# ['p', 'T', 'A', '$'] ['p', 'i', '$']
# ['T', 'A', '$'] ['i', '$']
# ['T', 'FB']
# ['F', 'B', 'A', '$'] ['i', '$']
# ['F', 'i']
# ['i', 'B', 'A', '$'] ['i', '$']
# ['B', 'A', '$'] ['$']
# ['B', 'abs']
# ['A', '$'] ['$']
# ['A', 'abs']
# ['$'] ['$']
# ['$'] ['$']
#
# Process finished with exit code 0


# "C:\Users\Austrin Dabre\PycharmProjects\ll1\venv\Scripts\python.exe" "C:/Users/Austrin Dabre/PycharmProjects/ll1/venv/ll1.py"
# Enter the number of rules : 5
# Rule 1 : S->ABCD
# Rule 2 : A->a|abs
# Rule 3 : B->CD|b
# Rule 4 : C->c|abs
# Rule 5 : D->Aa|d|abs
# ['S->ABCD', 'A->a|abs', 'B->CD|b', 'C->c|abs', 'D->Aa|d|abs']
# [['S', 'ABCD'], ['A', 'a', 'abs'], ['B', 'CD', 'b'], ['C', 'c', 'abs'], ['D', 'Aa', 'd', 'abs']]
# [False, True, False, True, False]
# ['S', 'A', 'B', 'C', 'D']
# [[], ['a', 'abs'], ['b'], ['c', 'abs'], ['d', 'abs']]
# ----------------------------------------------------------------------
# [[], ['a', 'abs'], ['b'], ['c', 'abs'], ['a', 'd', 'abs']]
# [[], ['a', 'abs'], ['d', 'b', 'c', 'a', 'abs'], ['c', 'abs'], ['a', 'd', 'abs']]
# [['d', 'b', 'c', 'a', 'abs'], ['a', 'abs'], ['d', 'b', 'c', 'a', 'abs'], ['c', 'abs'], ['a', 'd', 'abs']]
# First :
# [['d', 'b', 'c', 'a', 'abs'], ['a', 'abs'], ['d', 'b', 'c', 'a', 'abs'], ['c', 'abs'], ['a', 'd', 'abs']]
# Follow :
# Enter the start symbol : S
# [['$'], [], [], [], []]
# [['$'], ['d', 'b', 'c', '$', 'a'], ['a', 'd', 'c', '$'], ['a', 'd', 'c', '$'], ['a', 'd', 'c', '$']]
# ----------------------------------PARSING TABLE--------------------------------------------------------
# Firstc :   [['d', 'b', 'c', 'a', 'abs'], ['a', 'abs'], ['d', 'b', 'c', 'a', 'abs'], ['c', 'abs'], ['a', 'd', 'abs']]
# Follow :   [['$'], ['d', 'b', 'c', '$', 'a'], ['a', 'd', 'c', '$'], ['a', 'd', 'c', '$'], ['a', 'd', 'c', '$']]
# Terminal List :  ['a', 'b', 'c', 'd', '$']
# Non Terminal list :  ['S', 'A', 'B', 'C', 'D']
#        ['a', 'b', 'c', 'd', '$']
# ['S', ['S->ABCD'], ['S->ABCD'], ['S->ABCD'], ['S->ABCD'], ['S->ABCD']]
# ['A', ['A->abs', 'A->a'], ['A->abs'], ['A->abs'], ['A->abs'], ['A->abs']]
# ['B', ['B->CD'], ['B->b'], ['B->CD'], ['B->CD'], ['B->CD']]
# ['C', ['C->abs'], [], ['C->c', 'C->abs'], ['C->abs'], ['C->abs']]
# ['D', ['D->abs', 'D->Aa'], [], ['D->abs'], ['D->d', 'D->abs'], ['D->abs']]
# LL(1) is not possible
#
# Process finished with exit code 0
#
#
#
#
#
#
#

