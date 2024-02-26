import heapq

#n: 도시 개수, m: 통로 개수, c: 메시지 보내는 도시
n,m,start=map(int,input().split())

#n,m의 범위가 크므로 다익스트라 사용
INF=int(1e9)
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))


def solution(start):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,city=heapq.heappop(q)

        if distance[city]<dist:
            continue

        #현재 노드와 연결된 인접노드 확인
        for i in graph[city]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

solution(start)

cnt=0
max_distance=0
for d in distance:
    if d!=INF:
        cnt+=1
        max_distance=max(d,max_distance)

print(cnt-1,max_distance)

'''
3 2 1
1 2 4
1 3 2
'''