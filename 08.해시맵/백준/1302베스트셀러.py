n=int(input())
arr={}

for _ in range(n):
    x=input()
    
    if x in arr:
        arr[x]+=1
    else:
        arr[x]=1
        
# print(max(arr,key=arr.get)) # 틀림
'''
가장 많이 팔린 갯수가 여러 개인 경우 사전순으로 앞선 제목 찾아야함
'''

max_cnt=max(arr.values())
answer=min([k for k,v in arr.items() if v==max_cnt])
print(answer)
