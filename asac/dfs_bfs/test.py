# bfs로 탐색하는 함수
# 입력 : 출발점에 대한 정보(row, col) 좌표
# 기능 : 출발점에서 이동이 가능하다면,,,,,모두 이동하고, 체크하겠다!!
#        BFS 방식으로 다 체크하겠다!!!!!
# 출력 : 출발점에서 시작할 수 있고, 그래서 다 방문/탐색이 끝나면 1
#        출발점에서 시작할 수 없다면,,       
# 문제 조건 세팅
graph =[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
n = 4
m = 5
from collections import deque

def ice_bfs(row_init, col_init):
    # 1) 주어진 시작점 좌표가 시작할 수 있는지 없는지 체크!!!!!
    if graph[row_init][col_init]==0: # 시작이 가능한!!!!
        # 2) 방문할 곳들에 대한 : 할 일에 대한 초기 세팅!!!!!!
        
        q = deque([row_init, col_init])
        
        #graph[row_init][col_init] = 1
        # --> 위에 초기 시작 점에 대한 도장을 할지 말지 체크!!!
        #     오해없이 하기 위해서는 찍고 가는 것을 추천!!!!!!

        # 참고) 한 일 graph에 직접 0을 1로 바꿔가면서 진행을 하려고 함!!!
        while True: # ---> 무한 루프........빠져나갈 세팅!!!!!
            # 종료 조건!!!! : q가 빈 값이 될 때 까지..
            if not q:
                return 1 # 시작은 가능하고, 할 것 다하고,,최종 결과 1
            # ---> 할 일에 대한 본격 세팅
            # 갈 곳에 대한 선택
            row, col = q.popleft() # bfs --> 왼쪽에서 선택, dfs--> q.pop()
            print(row,col)
            # 직접 LRUD에 대해서 이동에 대한 체크!!!!!!!!
            for dx, dy in [ [0,-1], [0,1], [1,0], [-1,0]]:
                # ---> 이동 가능한지 체크!!!! in/ out
                if 0 <= row+dx < n and 0 <= col+dy < m: # 지도 안
                    # ---> 얼릴 수 있는지 체크 : 1/0
                    if graph[row+dx][col+dy] == 0:
                        graph[row+dx][col+dy] = 1
                        q.append( [row+dx, col+dy ])

    else:
        # 주어진 좌표에서 시작조차 할 수 없는 시작점
        return 0
    
result = 0 # 출력을 하는 카운팅 변수!!!!!
for row in range(n):
    for col in range(m):
        # 시작점 후보 (n,m)
        # if 시작할 수 있고, 탐색이 끝나면,,
        #  +1 카운팅 갱신!!!!!
        # ice_bfs(row, col)
        result += ice_bfs(row, col)
print(result)