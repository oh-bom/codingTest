id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#report 이용자,신고당한사람 순서
k=2

id_list2=["con", "ryan"]
report2=["ryan con", "ryan con", "ryan con", "ryan con"]
k2=3

def solution(id_list, report, k):
    user_list={id:{"reporters":set(),"email":0} for id in id_list}
    
    #key: 신고당한 사람, value: 신고한 사람들
    for line in report:
        user1,user2=map(str,line.split(" "))
        
        user_list[user2]["reporters"].add(user1)
        
    for key in user_list:
        if len(user_list[key]["reporters"])>=k:
            for user in user_list[key]["reporters"]:
                user_list[user]["email"]+=1
                
    return [value["email"] for value in user_list.values()]
    
    
    
print(solution(id_list,report,k))