num=(input())

result=int(num[0])
    
for i in range(1,len(num)):#int는 for문 못돌리니까 int로 형변환을 하지는 x
    if num[i]=="0" or result<1: #result<1인 경우도 추가
        result+=int(num[i])
    else:
        result*=int(num[i])

print(result)


