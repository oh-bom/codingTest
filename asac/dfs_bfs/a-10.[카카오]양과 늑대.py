# https://school.programmers.co.kr/learn/courses/30/lessons/92343

#info 0:양, 1:늑대
#edges [부모,자식]
sheep,wolf=0,0
temp_wolf,temp_sheep=0,0
        
info=[0,0,1,1,1,0,1,0,1,0,1,1]
edges=[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
def dfs(graph,i):
    global sheep,wolf,temp_sheep,temp_wolf
    
    if graph[i][0]==0:sheep+=1
    elif graph[i][0]==1:wolf+=1
    
    child_node=graph[i][1]
    print("index:",i,"s:",sheep,"w:",wolf)
    
    for child in child_node:
        if graph[child][0]==0:
            temp_sheep=sheep
            temp_sheep+=1
        elif graph[child][0]==1:
            temp_wolf=wolf
            temp_wolf+=1
        
        print("child:",child,"s:",temp_sheep,"w:",temp_wolf)
    
        if temp_sheep>temp_wolf:
            dfs(graph,child)


    
def solution(info, edges):
    answer = 0
    graph={}
    
    #[양,늑대],[연결된 자식 노드]
    for index in range(len(info)):
        child=[x[1] for x in edges if x[0]==index]
        graph[index]=[info[index],child]
        
    dfs(graph,0)
    
    print(sheep)
    
    
    
    return sheep

print(solution(info,edges))