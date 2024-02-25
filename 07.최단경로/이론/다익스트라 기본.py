import sys
input=sys.stdin.readline
INF=int(1e9) #무한, 10억

#노드, 간선
n,m=map(int,input().split())

#시작 노드 번호
start=int(input())

#각 노드에 연결된 노드에 대한 정보
graph=[[] for _ in range(n+1)]

visited=[False]*(n+1)

distance=[INF]*(n+1) #최단거리 테이블

#간선 정보 입력받기
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #a번 노드에서 b노드로 가는 비용-> c

#방문하지 않은 노드에서 가장 최단거리 짧은 노드 반환
def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start):
    #시작노드 초기화
    distance[start]=0
    visited[start]=True
    
    for j in graph[start]:
        distance[j[0]]=j[1]

    #시작노드 제외한 n-1개의 노드에 대해 반복
    for _ in range(n-1):
        now=get_smallest_node()
        visited[now]=True

        #현재 노드와 연결된 다른 노드 확인
        for i in graph[now]:
            cost=distance[now]+i[1]

            if cost<distance[i[0]]:
                distance[i[0]]=cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("도달 불가")
    else:#도달 가능 경우
        print(distance[i])

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3 
2 4 2
3 2 3
3 6 5
4 3 3 
4 5 1
5 3 1
5 6 2
'''