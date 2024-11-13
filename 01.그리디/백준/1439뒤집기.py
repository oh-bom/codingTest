# https://www.acmicpc.net/problem/1439

# nums=list(map(int,input().split()))
nums=input()
nums="11001100110011000001"
num_dic={"0":0,"1":0}

prev=nums[0]
num_dic[nums[0]]+=1

for now in nums:
    if now!=prev:
        num_dic[now]+=1
        prev=now
        
print(min(num_dic.values()))
# print(min(num_dic,key=num_dic.get)) # value 기준으로 min 고를때의 key값
            
