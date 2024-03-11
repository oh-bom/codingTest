n=int(input())

data=[]

for _ in range(n):
    data.append(int(input()))

data.sort()

cnt=0
sum=data[0]
for i in range(1,len(data)):
    sum+=data[i]
    cnt+=sum
print(cnt)
