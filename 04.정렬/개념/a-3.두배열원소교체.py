arr=[]
arr2=[]

n,k=map(int,input().split())
# arr.append(int(input().split(' ')))
# arr2.append(int(input().split(' ')))
arr=list(map(int,input().split()))
arr2=list(map(int,input().split()))

arr.sort()
arr2.sort()
print(arr,arr2)

# for i in range(n-1,n-k,-1):
#     arr[i],arr2[i]=arr2[i],arr[i]

for i in range(k):
    arr[i],arr2[n-1-i]=arr2[n-1-i],arr[i]

result=0
for i in range(n):
    result+=arr[i]

print(result)

#solution
arr.sort()
arr2.sort(reverse=True)

for i in range(k):
    arr[i],arr2[i]=arr2[i],arr[i]

'''
5 3
1 2 5 4 3
5 5 6 6 5
'''