#https://school.programmers.co.kr/learn/courses/30/lessons/17686?language=python3

import re

files= ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files2=["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
def solution(files):
    answer = []
    
    file_dict={}
    
    for file in files:
    
        number=re.search("(\d)+",file)
        # number=re.findall(r"\d+",file)[0]
        
        number_index=number.start() #시작 인덱스 반환
        number=number.group() #매치된 문자열 반환
        
        number=int(number) #00721 와 같이 앞에 zero-padding된 숫자에서 앞의 0 제거
        
        head=re.findall("\D+",file) #숫자 외의 문자들을 모두 리턴
        print("head",head)
        
        head=file[:number_index]
        head=head.lower() #소문자로 통일
        
        file_dict[file]=[head,number] #딕셔너리에 추가
        #print("dict",file_dict.items())
        '''
        dict_items([(0, ['img', 12]), (1, ['img', 10]), (2, ['img', 2]), (3, ['img', 1]), (4, ['img', 1])])
        '''
        
    answer=sorted(file_dict.items(),key=lambda x: (x[1][0],x[1][1]))
    
    file_list=list(file_dict.items())
    file_list.sort(key=lambda x: (x[1][0],x[1][1]))
    
    answer=[ x[0] for x in answer]
    
    print(answer)
        
    return answer

print(solution(files2))