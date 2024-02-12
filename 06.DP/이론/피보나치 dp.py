#재귀함수 피보나치
def recursive_fibo(x):
    if x==1 or x==2:
        return 1
    return recursive_fibo(x-1)+recursive_fibo(x-2)

#memoization+
d=[0]*100

def fibo(x):
    print(x,d[x]) #6 5 4 3 2 1 2 3 4 
    if x==1 or x==2:
        return 1
    
    if d[x]!=0:
        return d[x]
    
    d[x]=fibo(x-1)+fibo(x-2)

    return d[x]

print(fibo(6))

'''
6=5+4
5=4+3->d[5]저장
4=3+2->d[4]저장
3=2+1->d[3]저장

'''