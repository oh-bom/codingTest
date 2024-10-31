n=int(input())

a_arr=list(map(int,input().split()))
b_arr=list(map(int,input().split()))

# a와 b를 모두 정렬한 리스트를 생성하고 거기서 작은 a x 작은 
'''
 sort와 sorted
 sort: 해당 리스트 정렬 후 리턴 x a.sort()
 sorted: 해당 리스트 정렬 후 리턴 0 sorted(a)

'''

a_sorted=sorted(a_arr)
b_sorted=sorted(b_arr,reverse=True)
answer=0

for i in range(n):
    answer+=a_sorted[i]*b_sorted[i]
    
print(answer)