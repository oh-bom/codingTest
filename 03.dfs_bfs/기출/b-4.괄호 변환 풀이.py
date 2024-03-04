#균형잡힌 문자열의 인덱스 반환
def find_balance(word):
    cnt=0
    for i in range(len(word)):
        if word[i]=="(":cnt+=1
        else:cnt-=1

        if cnt==0:return i

def check_right(word):
    cnt=0
    for x in word:
        if x=="(":cnt+=1
        else:
            if cnt==0 or cnt<0:return False
            cnt-=1

    return True

def solution(word):
    result=""
    if len(word)==0:return result

    index=find_balance(word)
    u=word[:index+1]
    v=word[index+1:]

    x=solution(v)
        
    if check_right(u):
        result+=(u+x)
        
    else:
        result+="("
        result+=x
        result+=")"

        # u=u[1:-1] #리스트로 만들어야 제거가능
        u=list(u[1:-1])
        # reverse=""
        # for x in u:
        #     if x=="(":reverse+=")"
        #     else:reverse+="("
        # result+=reverse
        for x in u:
            if x=="(":
                x=")"
            else:x="("
        result+="".join(u)

    return result

p="(()())()"       
print(solution(p))