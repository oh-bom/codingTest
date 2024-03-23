import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())

graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

'''
heapqueue가 min value heap이기때문에 get_smallest_node() 가 불필요
'''

def dijkstra(start):
    q=[]
    #heapq에 (거리,노드 번호) 순으로 넣기
    #heapq는 min heap이기 때문에 거리 순으로 자동 정렬 

    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        #이미 distance[now] 값이 업데이트 된 경우,heapq에 들어간 값보다 작게
        #distance가 업데이트 된 것이기 때문에 아래 과정을 진행하지 x
        if distance[now]<dist:
            continue 

        for i in graph[now]:
            cost=dist+i[1]

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))



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