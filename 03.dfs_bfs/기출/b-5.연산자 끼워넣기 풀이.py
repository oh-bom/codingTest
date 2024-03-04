n=int(input())
nums=list(map(int,input().split()))

add,sub,mul,div=map(int,input().split())

max_value=int(-1e9)
min_value=int(1e9)

def dfs(i,now):
    global min_value,max_value,add,sub,mul,div

    if i==n:
        min_value=min(min_value,now)
        max_value=max(max_value,now)
        print("min:",min_value,"max:",max_value)
    else:
        if add>0:
            add-=1
            dfs(i+1,now+nums[i])
            add+=1 #back tracking
        if sub>0:
            sub-=1
            dfs(i+1,now-nums[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1,now*nums[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1,int(now/nums[i]))
            div+=1

dfs(1,nums[0])

#중복 순열(product)사용 
            
from itertools import product
n=4
operators=list(product(['+','-','*','/'],repeat=n-1))

def calculate(nums,operators):
    min_value=int(1e9)
    max_value=int(-1e9)
    result=nums[0]
    for operator in operators:
        for i in range(1,len(nums)-1):
            if operator=="+":
                result+=nums[i]
            elif operator=="-":
                result-=nums[i]
            elif operator=="*":
                result*=nums[i]
            else:
                result=int(result/nums[i])
        min_value=min(min_value,result)
        max_value=max(max_value,result)

    print(min_value,max_value)
print(calculate(nums,operators))

        

