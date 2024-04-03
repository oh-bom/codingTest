
data =[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
n = 4
m = 5

def dfs(x,y):
    if x<=-1 or x>=n and y<=-1 and y>=m:return False
    if data[x][y]==0:
        data[x][y]=1
        
        dfs(x,y-1)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x+1,y)
        
        return True
    
    return False

def solution(n,m):
    result=0
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:result+=1
            
    return result

print(solution(n,m))
    