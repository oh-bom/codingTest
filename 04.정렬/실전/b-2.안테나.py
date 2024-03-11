#https://www.acmicpc.net/problem/18310

#내가 푼 코드..

n=int(input())
data=list(map(int,input().split()))

data.sort()
index=n//2
if index%2!=0:result=data[index]
else:
    resultA=0
    resultB=0
    for i in range(n):
        resultA+=abs(data[i]-data[index])
        resultB+=abs(data[i]-data[index-1])
    result=data[index] if resultA<resultB else data[index-1]
    print(resultA,resultB)

print(result)

#풀이

# 중간값(median)을 출력
print(data[(n - 1) // 2])
'''
짝수일때는 n//2랑 n//2-1 둘다 상관 없지만, 안테나 작은거부터 하라고 문제에서 제시

'''

