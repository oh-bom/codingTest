'''
내 코드랑 로직이 많이 다르지는 않다 
풀이가 좀 더 간결한듯
'''
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance=[-1]*(n+1)
distance[x]=0

q=deque([x]) #리스트에 요소 넣은 후 바로 초기화
while q:
    now=q.popleft()

    for i in graph[now]:
        if distance[i]==-1:#아직 방문하지 않은 경우
            #어짜피 시작한 노드에서부터 방문한 것이 최단일테니 내 코드처럼 min을 확인할 필요x
            #여기서는 min 확인대신 방문 체크를 통해 최소 거리를 구함
            distance[i]=distance[now]+1
            q.append(i)
