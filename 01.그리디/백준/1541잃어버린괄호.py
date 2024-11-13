# https://www.acmicpc.net/problem/1541
'''
'-'를 기준으로 나눠서 arr1에 저장
arr1에서는 +로 연결된 숫자들의 합을 구하여 이를 뺌
'''

arr1=input().split("-")
calculated=[]
answer=0
for group in arr1:
    sum=0
    nums=group.split("+")
    
    for num in nums:
        sum+=int(num)
    calculated.append(sum)
    
answer=calculated[0]

for i in range(1,len(calculated)):
    answer-=calculated[i]
    
print(answer)
    
        
    