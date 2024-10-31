n=int(input())
arr=[]

for i in range(n):
    arr.append(tuple(map(int,input().split())))
    
# 내가했던 접근법:
# 문제점: lined 배열을 엄청나게 숫자로 메모리할당해줘야 하는 문제 발생..
# lined=[]
# # lined=[]
# answer=0

# for start,end in arr:
#     line_length=end-start
#     cnt=0
#     for i in range(start,end):
#         lined[i]+=1
#         if lined[i]>1:cnt+=1
        
#     answer+=(line_length-cnt)

# print(answer)
    
# 풀이
arr.sort()
start,end=arr[0]
answer=0
# answer=end-start

for i in range(1,n):
    x,y=arr[i]
    
    if x<end:
        end=y
    else:
        answer+=(end-start)
        start,end=x,y
answer+=(end-start)
print(answer)