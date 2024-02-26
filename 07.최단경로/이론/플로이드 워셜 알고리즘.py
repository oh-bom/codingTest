INF=int(1e9)

n=int(input())
m=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]

#본인 to 본인은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]==0

#간선 정보 입력
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

#플로이드워셜
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])

#결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==1e9:
            print("도달불가")
        else:
            print(graph[a][b],end='')

    print()

'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''