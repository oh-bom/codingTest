
from collections import deque
def solution(tickets):
    
    answer=[]

    def bfs(start):
        q=deque()
        result=[]

        next_city=""
        for ticket in tickets:
            if(ticket[0]==start):
                if(next_city!=""):
                        dif=ord(next_city[0])-ord(ticket[1][0])
                        if(dif>0):next_city=ticket[1]
                else:next_city=ticket[1]
        q.append((ticket[0],ticket[1]))

        while q:
            s,f=q.popleft()
            print(s,f)
            result.append(s)

            next_city=""
            for ticket in tickets:
                if(ticket[0]==f):
                    if(next_city!=""):
                        dif=ord(next_city[0])-ord(ticket[1][0])
                        if(dif>0):next_city=ticket[1]
                    else:next_city=ticket[1]
                    
            q.append((f,next_city))

        return result
    answer=bfs("ICN")
    return answer

tickets=[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))

