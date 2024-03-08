#https://school.programmers.co.kr/learn/courses/30/lessons/60057

s="abcabcdede"
def solution(s):
    #압축이 아예되지 않을때는 원래 문자열 길이가 answer
    answer=len(s)
    #step=1 부터 시작해서 압축 단위 늘려가서 확인
    for step in range(1,len(s)//2+1):
        compressed=""
        pattern=s[0:step]
        cnt=1

        for j in range(step,len(s),step):
            temp=s[j:j+step]
            #패턴 일치-> 압축 가능
            if pattern==temp:cnt+=1

            #패턴이 불일치 -> 압축 불가
            else:
                compressed+=str(cnt)+pattern if cnt>=2 else pattern

                #동일 step 사이즈의 패턴을 새로 지정후 다음 문자열부터 확인하기 위해 초기화
                pattern=temp
                cnt=1
        
        #남은 문자열 추가->예를 들어 10사이즈인데 step=4였으면 마지막 2개 문자열 
        compressed+=str(cnt)+pattern if cnt>=2 else pattern

        answer=min(answer,len(compressed))

    return answer

print(solution(s))



            