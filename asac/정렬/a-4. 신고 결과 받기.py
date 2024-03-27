#https://school.programmers.co.kr/learn/courses/30/lessons/92334
id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#report 이용자,신고당한사람 순서
k=2

id_list2=["con", "ryan"]
report2=["ryan con", "ryan con", "ryan con", "ryan con"]
k2=3
def solution(id_list, report, k):
    
    report=set(report)
    report=list(report)
    
    #dictionary Key:사람 value:신고한, 신고당한
    result={}
    xxlist={}
    emailcnt={}
    for id in id_list:
        xxlist[id]=0
        emailcnt[id]=0
    # xxlist={"muzi":0,"frodo":0,"apeach":0,"neo":0}
    
    # emailcnt={"muzi":0,"frodo":0,"apeach":0,"neo":0}
    
    for id in id_list:
        temp_list=[]
            
        for line in report:
            user1,user2=map(str,line.split(" "))
            if id==user1:
                temp_list.append(user2)
                xxlist[user2]+=1
                
        if temp_list:
            set_temp_list=set(temp_list)
            temp_list=list(set_temp_list)
            result[id]=temp_list
        
            print("result",result)
        
    for x in xxlist.items():
        print(x[1],k)
        if x[1]>=k:
            s=x[0] #신고 횟수 넘은 사람
            for y in result.items():
                cntlist=list(y[1])
                print(cntlist)
                if cntlist.count(s)>0:emailcnt[y[0]]+=1
                
    print(emailcnt)
    
    return [x for x in emailcnt.values()]
print(solution(id_list,report,k))