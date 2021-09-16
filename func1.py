import string

file_name=input()
complete_level=input()
file = open(file_name, "r", encoding='utf-8')
article = file.read()
article = article.replace(",","").replace(".","").replace("{"," ").replace("}"," ") \
    .replace(":","").replace(";","").replace("?","").replace("("," ").replace(")"," ")
#exchange = article.lower()#转成小写字母
count = article.split()#生成单词列表
exclude = ["auto","break","case","char","const","continue","default","do","double","else","enum","extern",
           "float","for","goto","if","int","long","register","return","short","signed","sizeof","static",
           "struct","switch","typedef","union","unsigned","void","volatile","while"]#关键词列表
dic={}
for word in count:
    if len(word)<2:#关键字没有单个字符的，可以排除
        continue
    else:
        dic[word]=dic.get(word,0)+1#如果字典里键为word的值存在，则返回键的值并加一，不存在，则返回0再加1
for key in list(dic.keys()): #遍历字典的所有键，即所有word
    if key not in exclude:
        del dic[key]
total_num=0
for value in list(dic.values()):
    total_num+=value

print("total num: ",total_num)
print("switch num: ",dic["switch"])