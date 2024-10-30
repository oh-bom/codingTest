# https://www.acmicpc.net/problem/2306


# 처음에 시도했던 코드 ( 그리디 ) -> 틀림 
dna=(input())
answer=0

# a가 나오기 전까지는 t 나오면 빼기, g 나오기 전까지 c가 나오면 빼기
dna_dic={"a":0,"t":0,"g":0,"c":0}

for i in dna:
    dna_dic[i]+=1
    if i=="t":
        if dna_dic["a"]<dna_dic[i]: # t가 삭제되어야 하는 경우
            dna_dic[i]-=1
            answer+=1 # 빼야 하는 t 수 증가
        else: #a-t 매칭
            dna_dic["a"]-=1
            dna_dic["t"]-=1
    
    elif i=="c":
        if dna_dic["g"]<dna_dic[i]:
            dna_dic[i]-=1
            answer+=1
        else:
            dna_dic["c"]-=1
            dna_dic["g"]-=1
            
    print(dna_dic)


for k,v in dna_dic.items():
    if v!=0:answer+=v
print(len(dna)-answer)
    
    
# gpt 풀이 - dp ver
dna=(input())
n=len(dna)

# dp[i][j]= i부터 j까지 부분 문자열에서 최대 유효 유전자 길이
dp=[[0]*n for _ in range(n)]

# 부분 문자열의 길이 2부터 n까지 순서대로 처리
for length in range(2, n + 1):  # 부분 문자열의 길이: 2 ~ n
    for i in range(n - length + 1):  # 시작 인덱스 i
        j = i + length - 1  # 끝 인덱스 j

        # dna[i]와 dna[j]가 유효한 쌍을 이루는 경우
        if (dna[i] == 'a' and dna[j] == 't') or (dna[i] == 'g' and dna[j] == 'c'):
            dp[i][j] = dp[i + 1][j - 1] + 2  # 쌍을 이루면 +2

        # 유효한 쌍이 아닌 경우, 두 선택지 중 최대값을 저장
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

# 0부터 n-1까지의 전체 문자열에서 최대 유효 유전자 쌍 길이 출력
print(dp[0][n - 1])