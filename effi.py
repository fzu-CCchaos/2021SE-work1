#!/usr/bin/env python
import profile
import string
import os
import re


def efficient_test():
    file_path = input()
    complete_level = 4
    exam_file(file_path)
    for x in '10000000':
        print("total num: ", get_total_num(file_path)[0])
        print("switch num: ", get_total_num(file_path)[1])
        print("case num:", end=" ")
        for i in get_case_num(file_path):
            print(i, end=' ')
        print()
        print("if-else num: ", get_ifelse_num(file_path))
        print("if-elseif-else num: ", get_elif_num(file_path))

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
        article_lines = f.readlines()
        for line in article_lines:
            line=line.replace(",","").replace(".","").replace("{"," ").replace("}"," ") \
                .replace(":","").replace(";","").replace("?","").replace("("," ").replace(")"," ")
            line = re.sub("//.*", "", line)
            line1=''.join(line)
            if line1.find("switch")!=-1:
                case_num.append('1')
            elif line1.find("case")!=-1:
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
        article_lines = f.readlines()
        for line in article_lines:
            line=line.replace(",","").replace(".","").replace("{"," ").replace("}"," ") \
                .replace(":","").replace(";","").replace("?","").replace("("," ").replace(")"," ")
            line = re.sub("//.*", "", line)
            line1 = ''.join(line)
            if line1.find("else if") != -1:
                if_else_num.append('0')
            elif line1.find("if") != -1:
                if_else_num.append('1')
            elif line1.find("else") != -1:
                if_else_num.append('2')
            else:
                continue

    if_else_total = 0
    for i in range(len(if_else_num)):
        if if_else_num[i] == '1' and if_else_num[i+1] == '2':
            if_else_total += 1
    return if_else_total


def get_elif_num(filename):
    if_elif_num = []
    with open(filename,'r') as f:
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
    flag_elif = 0  # 用来记录当前总的else if数量
    num_of_elif = 0  # 用来记录当前这个结构中 else if的数量

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
    return if_elif_total


if __name__ == "__main__":
    profile.run("efficient_test()")
    #efficient_test()
