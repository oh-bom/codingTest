
'''
graph=[]
for i in range(8):
    graph[i].append()
'''

'''
2 3 8
1 7
1 4 5
3 5
3 4
7
2 6 8
1 7
'''
n=8
graph=[[],
       [2,3,8],
       [1,7],
       [1,4,5],
       [3,5],
       [3,4],
       [7],
       [2,6,8],
       [1,7]
       ]

visited=[False]*(n+1)

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end='')

    #현재 노드와 연결된 다른 노드 재귀적 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)