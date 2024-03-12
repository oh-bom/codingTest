n=int(input()) #보드 크기
k=int(input()) #사과 개수

board=[[0]*n for _ in range(n)]
for _ in range(k):
    x,y=map(int,input().split())
    board[x][y]=1

d=int(input()) #뱀의 방향변환

snake_turn=[]
for _ in range(d):
    t,direction=(map(str,input().split()))
    snake_turn.append([int(t),direction])

snake_turn=dict(snake_turn)



from collections import deque
def solution(board):
    direction=[[0,1],[1,0],[0,-1],[-1,0]] #index: 0,1,2,3
    # dleft=[[0,1],[-1,0],[0,-1],[1,0]] #index:-4,-3,-2,-1
    q=deque()
    q.append((0,0,0,0,[0,1]))
    board[0][0]=2 #뱀의 몸통이 있는곳을 2로 할당

    # q=deque((0,0,1,0,0)) #(x,y,시간,방향인덱스,현재)->이렇게 한번에 하면 에러뜬다
    
    while q:
        x,y,time,index,temp=q.popleft()
        board[x][y]=2
        #test
        for i in range(n):
            print(board[i])
        print(" ")
        
        #방향 전환 시간일때
        if time in snake_turn:
            d=snake_turn[time]

            if d=="D":index+=1
            else:index-=1
            
            index=abs(index%4)
            print(index)
            temp=direction[index]

        
        
        #단순 이동
        nx=x+temp[0]
        ny=y+temp[1]

        #벽과 부딪힐때 체크
        if 0<=nx<n and 0<=ny<n and board[nx][ny]!=2:
            #사과 만났을때
            if board[nx][ny]!=1:board[x][y]=0   
            
            q.append((nx,ny,time+1,index,temp))
            
        
                
    return time+1

print(solution(board))
