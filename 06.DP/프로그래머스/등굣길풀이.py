def solution(m, n, puddles):
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    grid[1][1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if [x, y] in puddles:
                continue
            b1 = grid[y - 1][x]
            b2 = grid[y][x - 1]
            if [x, y - 1] in puddles:
                b1 = 0
            if [x - 1, y] in puddles:
                b2 = 0
            grid[y][x] += b1 + b2
    answer = grid[n][m] % 1000000007
    return answer


def solution(M, N, puddles):
    roads = [[0 for _ in range(M+1)] for _ in range(N+1)]   #dp

    for puddle in puddles:
        roads[puddle[1]][puddle[0]] = -1           #puddle 위치 표시

    for i in range(1,N+1):
        for j in range(1,M+1):
            if i==1 and j==1:                 
                roads[1][1] = 1                    #시작 = 1
            elif roads[i][j] == -1:                 # puddle일경우 0으로 바꾸기
                roads[i][j] = 0
            else:                                  #dp 더하기
                roads[i][j] = roads[i-1][j]+roads[i][j-1]
    return roads[N][M] % 1000000007

def solution(n,m,puddles):
    graph=[[0]*(m+1) for _ in range(n)]
    
    for p in puddles:
        graph[p[1]][p[0]]=-1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:graph[1][1]=1
            elif graph[i][j]==-1:continue
            else: graph[i][j]=graph[i-1][j]+graph[i][j-1]
            
    return graph[n][m]%1000000007
