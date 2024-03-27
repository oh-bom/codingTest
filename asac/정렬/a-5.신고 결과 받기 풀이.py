#report (신고한사람, 신고당한 사람)

id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#report 이용자,신고당한사람 순서
k=2

id_list2=["con", "ryan"]
report2=["ryan con", "ryan con", "ryan con", "ryan con"]
k2=3

def solution(id_list, report, k):
    answer_dict={ id:set() for id in id_list}
    email_dict={ id:0 for id in id_list}
    
    #key: 신고당한 사람, value: 신고한 사람들
    for line in report:
        user1,user2=map(str,line.split(" "))
        
        answer_dict[user2].add(user1)
        
    print(answer_dict)

    #신고횟수가 k이상인지
    # for answer in answer_dict.items():
    #     if len(answer[1])>=k:
            
    k_reported=[key_id for key_id,v in answer_dict.items() if len(v)>=k]
    
    for key,v in answer_dict.items():
        if len(v)>=k:
            #신고한 사람의 cnt를 증가
            # for x in list(answer[1]):
            for x in list(v):
                email_dict[x]+=1
                
    print(email_dict)  

    return [ x for x in email_dict.values()]

print(solution(id_list,report,k))