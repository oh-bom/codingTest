n=int(input())
arr=list(map(int,input().split()))
time=[]
total=0

arr.sort()

for x in arr:
    total+=int(x)
    time.append(total)
print(sum(time))