# 참고 : https://velog.io/@op032/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A8%EC%96%B4-%EB%B3%80%ED%99%98python
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

'''
bfs자체가 너비 우선이니까,, 요기서 나오는 거리가 최단거리일수밖에없당 굳이 min으로 찾지않아도 됨
'''

from collections import deque

def solution(begin,target,words):
    
    if target not in words:return 0
    q=deque([begin,0])
    
    visited=[0]*(len(words))
    
    while q:
        word,cnt=q.popleft()
        if word==target:
            return cnt
            
        for index,temp_word in enumerate(words):
            temp_cnt=0
            
            if not visited[index]:
                for x,y in zip(word,temp_word):
                    if x!=y:temp_cnt+=1
                if temp_cnt==1:
                    q.append([temp_word,cnt+1])
                    visited[index]
                  

begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin,target,words))

