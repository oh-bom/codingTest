import itertools

num,game_type=map(str,input().split())
num=int(num)

people={}
games={"Y":2,"F":3,"O":4}
for i in range(num):
    id=input()
    # if id not in people:people.append(id)
    if id not in people:people[id]=1

def solution(num,game_type,people):
    
    game_cnt=games[game_type]-1

    return int(len(people)/game_cnt)
print(solution(num,game_type,people))



