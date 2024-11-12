# https://www.acmicpc.net/problem/2644
from collections import deque

n=int(input())
targetx,targety=map(int,input().split())
m=int(input())

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def solution(targetx,targety,graph):
    
    def dfs(targetx,targety,cnt):
        # graph[1]=[2, 3]
        
        if targetx==targety:return cnt
        
        for p in graph[targetx]:
            # if p==targety:return cnt
            if graph[p] and not visited[p]:
                visited[p]=True
                result=dfs(p,targety,cnt+1)
                if result!=-1:
                    return result
                # visited[p]=False
        
        return -1
    
    def bfs(targetx,targety):
        deq=deque([[targetx,0]])
        
        while deq:
            now,cnt=deq.popleft()
        
            if now==targety:return cnt
            
            for p in graph[now]:
                if graph[p] and not visited[p]:
                    visited[p]=True
                    deq.append([p,cnt+1])
                    
        return -1
                
    
    # print(dfs(targetx,targety,0))
    print(bfs(targetx,targety))
    
solution(targetx,targety,graph)

'''
dfs는 깊이별로 들어가니까 cnt를 인자로 관리해서 세는게 맞고
bfs는 너비로 가니까 한 단계에 여러개의 노드들이 추가되지 그러면 노드마다의 cnt로
관리해야징
'''