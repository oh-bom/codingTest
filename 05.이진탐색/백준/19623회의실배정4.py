
n=int(input())

arr=[]
min_val=int(1e9)
max_val=-int(1e9)

dp_set=[]
for _ in range(n):
    x,y,p=map(int,input().split())
    arr.append([y,-p,x])
    
    dp_set.append(x)
    dp_set.append(y)
    
dp_set=set(dp_set)
dp={}
dp[0]=0

for x in dp_set:
    if x not in dp:dp[x]=0

prev=0
answer=0
arr.sort()

for x in arr:
    end,p,start=x
    p=(-p)
    

    if prev<start:
        dp[end]=max(dp[end],dp[prev]+p)
        prev=end
        
print(max(dp))
    
# 풀이
import bisect

n = int(input())
meetings = []

for _ in range(n):
    start, end, people = map(int, input().split())
    meetings.append((end, start, people))

# 종료 시간 기준으로 정렬
meetings.sort()

# 종료 시간만 모은 리스트
end_times = [meetings[i][0] for i in range(n)]

# DP 배열 초기화
dp = [0] * n
dp[0] = meetings[0][2]

for i in range(1, n):
    end_i, start_i, people_i = meetings[i]
    
    # 이진 탐색으로 겹치지 않는 이전 회의 찾기
    idx = bisect.bisect_right(end_times, start_i) - 1
    
    # idx가 유효하고 겹치지 않는 회의인 경우만 dp 갱신
    if idx >= 0 and end_times[idx] <= start_i:
        dp[i] = max(dp[i-1], dp[idx] + people_i)
    else:
        dp[i] = max(dp[i-1], people_i)

print(max(dp))

        
    
    