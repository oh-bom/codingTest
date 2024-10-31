n=int(input())
people={}

for _ in range(n):
    name,state=map(str,input().split())
    people[name]=state
    
answer=[]
remained=[k for k,v in people.items() if v=="enter"]

for x in sorted(remained,reverse=True):
    print(x)