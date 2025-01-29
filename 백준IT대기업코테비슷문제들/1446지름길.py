#https://www.acmicpc.net/problem/1446

n,d=map(int,input().split())

# v1:내가 푼 코드 틀림 ^_^
# dp=[int(1e9)]*dis
# dp[0]=0
# ans=0
# last=0
# for i in range(n):
#     start,end,d=map(int,input().split())
    
#     if (last==0 and start!=0):ans+=(start-last) # 맨 처음
#     elif(last<start and last!=0):ans+=(start-last) #지름길 없이 간 거리
    
#     elif end>dis: # 전체 걸이보다 넘치는 경우 사용할수없음
#         break
#     else:
#         dp[end]=min(dp[end],dp[last]+d)
#         last=end
#     print("ans:",ans)
        
# ans+=(dis-last) # 지름길 후에 남은 거리
# ans+=(dp[last]) #지름길로 간 거리 추가
# print(ans)

# v2:풀이 코드 (dp)
dp=[i for i in range(d+1)]

shortcuts=[]

for _ in range(n):
    start,end,dis=map(int,input().split())
    if end-start>dis:
        shortcuts.append([start,end,dis])
        
shortcuts.sort()

for start,end,dis in shortcuts:
    for i in range(1,d+1):
        if end==i:
            dp[i]=min(dp[i],dp[start]+dis)
        else:
            dp[i]=min(dp[i],dp[i-1]+1)
            
print(dp[d])

# v3: 풀이코드 (다익스트라)
import heapq
n,d=map(int,input().split())
graph=[[] for _ in range(d+1)]
dist=[int(1e9)]*(d+1)

for i in range(d):
    graph[i].append((i+1,1))
    
for _ in range(n):
    start,end,dis=map(int,input().split())
    
    if dis<=d:graph[start].append((end,dis))
    
q=[]
heapq.heappush(q,(0,0)) # 거리,노드
dist[[0]]=0

while q:
    d,node=heapq.heappop(q)
    
    for e,dd in graph[node]:
        cost=dist[node]+dd
        if dist[e]>cost:
            dist[e]=cost
            heapq.heappush(q,(cost,e))
            
print(dist[d])