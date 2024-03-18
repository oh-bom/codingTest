n,m=map(int,input().split())
INF=int(1e9)
arr=[]

#input입력 ver1
for _ in range(n):
    arr.append(list(map(int,input().split())))

home_arr=[]
chicken_arr=[]

for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            chicken_arr.append([i,j])
        elif arr[i][j]==1:
            home_arr.append([i,j])

#위의 과정 좀 더 효율적으로
#input 입력 ver2
for i in range(n):
    data=list(map(int,input().split()))
    for j in range(n):
        if data[j]==1:
            home_arr.append((i,j))
        elif data[j]==2:
            chicken_arr.append((i,j))


from itertools import combinations
def cal_distance(chickens,home_arr):
    city_distance=0

    #각각의 집에 해당하는 치킨 거리 구하기
    for home in home_arr:
        hx,hy=home
        temp=0
        distance=INF

        for chicken in chickens:
            cx,cy=chicken
            temp=abs(hx-cx)+abs(hy-cy)
            distance=min(distance,temp)
    
        city_distance+=distance

    return city_distance

def solution(chicken_arr,home_arr,m):
    dist=INF
    chickens=combinations(chicken_arr,m)
    
    for case in chickens:
        temp=cal_distance(case,home_arr)
        dist=min(dist,temp)

    return dist


print(solution(chicken_arr,home_arr,m))
'''
치킨 집 위치를 따로 저장해두고 combination으로 고르기
그거마다의 치킨거리 계산후 min update
'''