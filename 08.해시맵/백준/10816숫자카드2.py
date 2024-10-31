n=int(input())
a=list(map(int,input().split()))

m=int(input())
b=list(map(int,input().split()))

owned_dic={}
answer=[]

for x in a:
    if x not in owned_dic:
        owned_dic[x]=1
    else:
        owned_dic[x]+=1
        
for x in b:
    if x not in owned_dic:
        answer.append(str(0))
    else: answer.append(str(owned_dic[x]))
    
print(" ".join(answer))