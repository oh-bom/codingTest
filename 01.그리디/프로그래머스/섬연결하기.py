# https://school.programmers.co.kr/learn/courses/30/lessons/42861#qna
# 정답
def solution(n,costs):
    answer=0
    uni=[0]*(n+1)
    
    for i in range(n):uni[i]=i
    costs.sort(key=lambda x:x[2])
    
    def find(x):
        if uni[x]==x:return x
        else:
            uni[x]=find(uni[x])
            return uni[x]
        
    def union(x,y):uni[find(x)]=find(y)
            
    for x,y,cost in costs:
        if find(x)!=find(y):
            union(x,y)
            answer+=cost
            
    return answer

def solution(n, costs):
    answer = 0
    uni=[0]*(n+1)
    costs.sort(key=lambda x:x[2])
    
    for i in range(n):
        uni[i]=i
    
    def find(x):
        if uni[x]==x:return x
        else:
            uni[x]=find(uni[x])
            return uni[x]
    
    def union(x,y):
        if find(x)!=find(y):
            uni[find(x)]=find(y)
            
    for n1,n2,cost in costs:
        if find(n1)!=find(n2):
            union(n1,n2)
            answer+=cost
    
    return answer
        
    

# def solution(n, costs):
#     answer = 0
#     costs.sort(key=lambda x:x[2])
#     link=set([costs[0][0]])
    
#     while len(link)!=n:
#         for v in costs:
#             if v[0] in link and v[1] in link:
#                 continue
#             if v[0] in link or v[1] in link:
#                 link.update([v[0],v[1]])
#                 answer+=v[2]
#     return answer