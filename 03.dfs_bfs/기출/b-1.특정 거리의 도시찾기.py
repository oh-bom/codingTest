#https://www.acmicpc.net/problem/18352
#n : 도시 개수, m: 도로 개수, 거리정보:k, 출발도시:start
INF=int(1e9)
n,m,k,start=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
visited=[False]*(n+1)

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
print(graph)


from collections import deque

def solution(k,start):
    q=[]
    q=deque(q)
    distance[start]=0
    
    q.append((start,0))

    while q:
        x,dist=q.popleft()

        for i in graph[x]:
            # if not visited[i]:
                # dist+=1
                # distance[i]=dist
            distance[i]=min(distance[i],dist+1)
            q.append((i,distance[i]))

    result=[]
    for i in range(len(distance)):
        if distance[i]==k:
            result.append(i)
    
    if(len(result)==0):result.append(-1)

    return result


result=solution(k,start)
for i in result:
    print(i)



'''
4 4 2 1
1 2 
1 3
2 3
2 4
'''