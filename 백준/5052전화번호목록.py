# https://www.acmicpc.net/problem/5052

t=int(input())

# 내장함수 쓰는 코드
def check(arr):
    arr.sort()
    answer="YES"
    for i in range(len(arr)-1):
        if arr[i+1].startswith(arr[i]):answer="NO"
    
    return answer

result=[]
for _ in range(t):
    
    n=int(input())
    arr=[]
    for _ in range(n):
        arr.append(str(input()))
        
    result.append(check(arr))

for x in result:
    print(x)

# 내장함수 안쓰는 코드
def isPrefix(s1,s2): 
  
    for i in range(len(s1)):
       if s1[i]!=s2[i]:return False
    
    return True

def check2(arr):
    arr.sort()
    
    for i in range(len(arr)-1):
        if(isPrefix(arr[i],arr[i+1])):return "NO"
        
    return "YES"

result2=[]
for _ in range(t):
    
    n=int(input())
    arr=[]
    for _ in range(n):
        arr.append(str(input()))
        
    result2.append(check2(arr))

for x in result2:
    print(x)