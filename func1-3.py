import string
file_name=input()
complete_level=input()
def get_total_num(filename):
    file = open(filename, "r", encoding='utf-8')
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
    return [total_num,dic["switch"]]

def get_case_num(filename):
    case_num=[]
    case_num_list=[]
    with open(filename,'r') as f:
        for line in f:
            line1=line.strip().split('\n')
            line2=''.join(line1)#将list转为string
            if line2.find("switch")!=-1:
                case_num.append('1')
            elif line2.find("case")!=-1:
                case_num.append('2')
    i=0
    num_of_case=0
    for i in range(len(case_num)):
        if case_num[i]=='1' and num_of_case!=0:
            case_num_list.append(num_of_case)
            num_of_case=0
        elif case_num[i]=='2':
            num_of_case+=1
            if i==len(case_num)-1:
                case_num_list.append(num_of_case)
    return case_num_list

def get_ifelse_num(filename):
    if_else_num=[]
    with open(filename,'r') as f:
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
    return if_else_total

if complete_level=='1':
    print("total num: ",get_total_num(file_name)[0])
elif complete_level=='2':
    print("total num: ",get_total_num(file_name)[0])
    print("switch num: ",get_total_num(file_name)[1])
    print("case num:",end=" ")
    for i in get_case_num(file_name):
        print(i,end=' ')
elif complete_level=='3':
    print("total num: ",get_total_num(file_name)[0])
    print("switch num: ",get_total_num(file_name)[1])
    print("case num:",end=" ")
    for i in get_case_num(file_name):
        print(i,end=' ')
    print()
    print("if-else num: ",get_ifelse_num(file_name))