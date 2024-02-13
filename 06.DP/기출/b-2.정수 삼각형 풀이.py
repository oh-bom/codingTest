'''
내 풀이와 차이점
: 
1. 나는 dp에서 값이 없는 부분은 -1로 초기화 시켜주었는데 어짜피 dp 할때 없는 값들은 접근도 안하니까 상관x
2. max값 구하는 과정
'''

n = int(input())
dp = [] # 다이나믹 프로그래밍을 위한 DP 테이블 초기화

for _ in range(n):
    dp.append(list(map(int, input().split())))


#이 부분은 로직 동일
for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

#최대값 구하기
print(max(dp[n-1]))