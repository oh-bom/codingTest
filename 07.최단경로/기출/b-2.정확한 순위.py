n,m=map(int,input().split())
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1 #비교 가능한 학생들은 1로 세팅

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:graph[i][j]=0

#플로이드
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])


#정확한 위치를 알 수 있는 학생수
result=0

#학생마다 다른 학생에 도달가능한지 확인
for i in range(1,n+1):
    cnt=0
    for j in range(1,n+1):

        #i와 j의 키 대소관계를 파악가능한 경우
        #graph[i][j]:i<j, graph[j][i]:j<i
        #둘 중 하나라도 INF라는 건 둘 사이의 키의 관계가 명확하다는 의미
        if graph[i][j]!=INF or graph[j][i]!=INF:cnt+=1
        
    #본인 포함하여 n명의 위치가 INF가 아니라면
    if cnt==n:
        result+=1

print(result)

'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''