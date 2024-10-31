# union-find & dictionary
tc=int(input())
for _ in range(tc):
    n=int(input())
    name_list=[]
    uni={} # 부모 노드 담아둘 리스트
    size={} 
        
    def union(x,y):
        rootX=find(x)
        rootY=find(y)
        
        if rootX!=rootY:
            if rootX>rootY:
                uni[rootX]=rootY
                size[rootY]+=size[rootX]
            else:
                uni[rootY]=rootX
                size[rootX]+=size[rootY]
    
    def find(x):
        if uni[x]==x:return x
        else:
            uni[x]=find(uni[x])
            return uni[x]
        
    for i in range(n): 
        a,b=map(str,input().split())
        if a not in uni:
            uni[a]=a
            size[a]=1
        if b not in uni:
            uni[b]=b
            size[b]=1
         
        union(a,b)
        root=find(a)
        print(size[root])
        
        
    
        
    
        

    