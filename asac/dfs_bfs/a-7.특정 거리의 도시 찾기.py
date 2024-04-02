from collections import deque
n,m,k,start=map(int,input().split())

INF=float("inf")

data=[[] for _ in range(n+1)]

data1=[[0]*(n+1)] # q. 왜 [[0],[0]..] 형태가 아닐까

# [0]+[0]+[0] = [0,0,0 ]

print(data)
print(data1)

d=[-1]*(n+1)

for _ in range(m):
    x,y=map(int,input().split())
    # data[x].append((1,y)) #거리, 도달 위치
    data[x].append(y)
    
def solution(data,k,x):
    q=[]
    q=deque(q)
    
    d[x]=0
    q.append(x)
    
    while q:
        now=q.popleft()
        for x in data[now]:
        
            if d[x]==-1:
                d[x]=d[now]+1
                q.append(x)
                
    result=[]
    for index,dist in enumerate(d):
        if dist==k:
            result.append(index)
            
    #if len(result)==0:result.append(-1)
    if result==[]:result.append(-1)
   
    return result 
    # return [ index for index,dist in enumerate(d) if dist==k]
    
x=solution(data,k,start)

#출력 형태
for i in x:
    print(i)

while x:
    print(x.pop(0))
       
#print(solution(data,k,start))

# def solution(data,n,m,k,x):
    
#     for i in range(2,n+1):
#         for data in data[i]:
#             dist,location=data
#             d[location]=min(d[location],dist)