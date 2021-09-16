import string

file_name=input()

if_else_num=[]

with open(file_name,'r') as f:
    for line in f:
        line1=line.strip().split('\n')
        line2=''.join(line1)
        if line2.find("else if")!=-1:
            if_else_num.append('0')
        elif line2.find("if")!=-1:
            if_else_num.append('1')
        elif line2.find("else")!=-1:
            if_else_num.append('2')
        else:
            continue

if_else_total=0
for i in range(len(if_else_num)):
    if if_else_num[i]=='1' and if_else_num[i+1]=='2':
        if_else_total+=1
print("if-else num: ",if_else_total)