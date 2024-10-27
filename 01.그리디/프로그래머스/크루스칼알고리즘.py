#크루스칼 알고리즘은 최소 비용으로 모든 노드를 연결하는 최소 비용 신장 트리(MST, Minimum Spanning Tree
#union-find랑 연결됨
n=int(input())
parent=[i for i in range(n)]
    
def find(x): #귀적으로 부모 노드(루트 노드)를 찾는 함수
    if parent[x]!=x:
        parent[x]=find(parent[x]) # 부모를 따라가며 최종 루트를 찾음 (경로 압축)
        
    return parent[x]

'''
만약 노드 5의 부모가 4이고, 4의 부모가 3이라면
find(5)는 parent[5] = 4이므로 find(4)를 호출.
find(4)는 parent[4] = 3이므로 find(3)를 호출.
find(3)은 parent[3] = 3이므로 루트가 3임을 반환
'''

def union(a,b):
    rootA=find(a)
    rootB=find(b)
    
    if rootA<rootB:
        parent[rootB]=rootA
    else:
        parent[rootA]=rootB

def kruskal(n,edges):
    edges.sort(key=lambda x:x[2])
    total_cost=0
    
    for a,b,cost in edges:
       if find(a)!=find(b): # 여기서 같은 경우를 연결해야 사이클이 생김
           union(a,b)
           total_cost+=cost