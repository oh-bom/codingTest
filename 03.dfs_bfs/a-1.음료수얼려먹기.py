def dfs(x,y,n,m,data,result):
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    for dir in dirs:
        nx=x+dir[0]
        ny=y+dir[1]

        if(nx<0 or ny<0 or nx>=n or ny>=m):return False

        if(0<nx<n and 0<ny<m and data[nx][ny]==0):
            data[nx][ny]=1 ##
            dfs(nx,ny,n,m,data,result)
            return True ##
        return False
    
    


# def solution(n,m,data):
#     result=0
#     for i in range(n):
#         for j in range(m):
#             dfs(i,j,data,result)
#             result+=1
    
#     return result

    
n,m=map(int,input().split())
data=[]

for _ in range(n):
    data.append(list(map(int,input().split())))

result=0
for i in range(n):
    for j in range(m):

        if(dfs(i,j,n,m,data,result)):result+=1
    
print(result)

# print(solution(n,m,data))