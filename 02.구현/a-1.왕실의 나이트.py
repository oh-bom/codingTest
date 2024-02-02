#나의 끄적임
# data=str(input())
# col=int(ord(data[0])-ord('a'))
# row=int(data[1])
# col=int(col)
# cnt=8

# if row+2>8:cnt-=2
# if (row-2)<0:cnt-=2
# if (col+2)>8:cnt-=2
# if (col-2)<0:cnt-=2

# print(cnt)

#풀이

data=str(input())
col=int(ord(data[0])-ord('a'))
row=int(data[1])

dirs=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,2),(1,-2),(2,-1),(2,1)]

result=0
for dir in dirs:
    nx=row+dir[0]
    ny=row+dir[1]
    if(0<nx<9 and 0<ny<9):result+=1

print(result)



