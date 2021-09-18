import string
import re

file_name=input()

if_elif_num = []

with open(file_name,'r') as f:
    article_lines = f.readlines()
    for line in article_lines:
        line=line.replace(",","").replace(".","").replace("{"," ").replace("}"," ") \
            .replace(":","").replace(";","").replace("?","").replace("("," ").replace(")"," ")
        line = re.sub("//.*", "", line)
        line1 = ''.join(line)
        if line1.find("else if") != -1:
            if_elif_num.append('2')
        elif line1.find("if") != -1:
            if_elif_num.append('1')
        elif line1.find("else") != -1:
            if_elif_num.append('3')
        else:
            continue

if_elif_total = 0
flag_else = 0  # 用来记录当前有多少个else
flag_elif = 0  # 用来记录当前是否已经有一个else if
num_of_elif = 0

if_elif_num.reverse()  # 将list倒序
for i in range(len(if_elif_num)):
    if if_elif_num[i] == '3':
        flag_else += 1
    if if_elif_num[i] == '2':
        flag_elif += 1
        num_of_elif += 1
    if if_elif_num[i] == '1':
        if flag_else >= 1 and flag_elif >= 1:
            if_elif_total += 1
            flag_elif -= num_of_elif
        else:
            flag_else -= 1
            flag_elif -= 0


print("if-elseif-else num: ", if_elif_total)
