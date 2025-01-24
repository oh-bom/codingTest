# https://www.acmicpc.net/problem/23971
import math

h,w,n,m=map(int,input().split())

max_m=math.ceil((w)/(m+1))
max_n=math.ceil((h)/(n+1))

print(max_m*max_n)