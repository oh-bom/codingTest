n=int(input())

data=[]
for _ in range(n):
    input_data=input().split()
    data.append((input_data[0],int(input_data[1])))
    # data.append(list(map(str,input().split)))

def setting(data):
    return data[1]

result=sorted(data,key=setting)

result2=sorted(data,key=lambda student:student[1]) #student에 data를 받고 student[1] 리턴

print(result)
print(result2)