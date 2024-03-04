def check_balance(word):
    cnt=0
    result=""
    for x in word:
        if x=="(":
            cnt+=1
            result+=x
        elif x==")":
            cnt-=1
            result+=x

        if cnt==0:return result


def solution(p):
    answer = ''
    return answer