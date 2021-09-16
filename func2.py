import string

file_name=input()
complete_level=input()

case_num=[]
case_num_list=[]
with open(file_name,'r') as f:
    for line in f:
        line1=line.strip().split('\n')
        line2=''.join(line1)
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
print("case num:",end=" ")
for i in case_num_list:
    print(i,end=' ')