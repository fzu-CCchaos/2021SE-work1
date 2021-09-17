import string
import os
import re

file_name = input()
complete_level = input()

total_num = 0
dic = {}

exclude = ["auto","break","case","char","const","continue","default","do","double","else","enum","extern",
           "float","for","goto","if","int","long","register","return","short","signed","sizeof","static",
           "struct","switch","typedef","union","unsigned","void","volatile","while"]  # 关键词列表

file = open(file_name, "r", encoding='utf-8')
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
print("total num: ",total_num)
