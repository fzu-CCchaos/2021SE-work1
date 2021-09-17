import string
import os
import re

file_path = input()
complete_level = input()


# Detect whether the file path exists
def exam_file(filepath):
    if not os.path.exists(filepath):
        print("The file is not exist")
        exit(1)


# get the total num of key words
def get_total_num(filename):
    total_num = 0
    dic = {}

    exclude = ["auto","break","case","char","const","continue","default","do","double","else","enum","extern",
               "float","for","goto","if","int","long","register","return","short","signed","sizeof","static",
               "struct","switch","typedef","union","unsigned","void","volatile","while"]  # 关键词列表

    file = open(filename, "r", encoding='utf-8')
    article_lines = file.readlines()  # article_lines是list类型
    for line in article_lines:
        line=line.replace(",","").replace(".","").replace("{"," ").replace("}"," ") \
            .replace(":","").replace(";","").replace("?","").replace("("," ").replace(")"," ")
        line = re.sub("//.*", "", line)  # "."匹配除换行符以外的任意字符,"*"表示重复0或多次，sub是替换
        count = line.split()  # 每行都生成一个单词列表
        for word in count:
            if len(word) < 2:  # 关键字没有单个字符的，可以排除
                continue
            else:
                dic[word] = dic.get(word,0)+1  # 如果字典里键为word的值存在，则返回键的值并加一，不存在，则返回0再加1
    for key in list(dic.keys()):  # 遍历字典的所有键，即所有word
        if key not in exclude:
            del dic[key]
    for value in list(dic.values()):
        total_num += value
    return [total_num, dic["switch"]]


# get the number of switch-case group
def get_case_num(filename):
    case_num = []
    case_num_list = []
    with open(filename, 'r') as f:
        for line in f:
            line1 = line.strip().split('\n')
            line2 = ''.join(line1)  # 将list转为string
            if line2.find("switch") != -1:
                case_num.append('1')
            elif line2.find("case") != -1:
                case_num.append('2')
    i = 0
    num_of_case = 0
    for i in range(len(case_num)):
        if case_num[i] == '1' and num_of_case != 0:
            case_num_list.append(num_of_case)
            num_of_case = 0
        elif case_num[i] == '2':
            num_of_case += 1
            if i == len(case_num)-1:
                case_num_list.append(num_of_case)
    return case_num_list


# get the number of if-else group
def get_ifelse_num(filename):
    if_else_num = []
    with open(filename,'r') as f:
        for line in f:
            line1 = line.strip().split('\n')
            line2 = ''.join(line1)
            if line2.find("else if") != -1:
                if_else_num.append('0')
            elif line2.find("if") != -1:
                if_else_num.append('1')
            elif line2.find("else") != -1:
                if_else_num.append('2')
            else:
                continue
    if_else_total=0
    for i in range(len(if_else_num)):
        if if_else_num[i] == '1' and if_else_num[i+1] == '2':
            if_else_total += 1
    return if_else_total


exam_file(file_path)
if complete_level == '1':
    print("total num: ", get_total_num(file_path)[0])
elif complete_level == '2':
    print("total num: ", get_total_num(file_path)[0])
    print("switch num: ", get_total_num(file_path)[1])
    print("case num:", end=" ")
    for i in get_case_num(file_path):
        print(i, end=' ')
elif complete_level == '3':
    print("total num: ", get_total_num(file_path)[0])
    print("switch num: ", get_total_num(file_path)[1])
    print("case num:", end=" ")
    for i in get_case_num(file_path):
        print(i, end=' ')
    print()
    print("if-else num: ", get_ifelse_num(file_path))

elif complete_level > '4' or complete_level < '1':
    print("Treatment level is out of range,the range is from 1 to 4")
