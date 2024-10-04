# https://school.programmers.co.kr/learn/courses/30/lessons/84512#qna
from itertools import product

def solution(word):
    # 만들 수 있는 단어 중복 순열로 생성
    lis = list()
    words = ['A','E','I','O','U']
    word_list=[]
    for j in range(1,6):
        for i in product(words,repeat=j):
            lis.append(list(i))
    lis.sort()
      
    for i in lis:
        st="".join(i)
        word_list.append(st)
    return (word_list.index(word)+1)
        
def solution(word):
    temp_list=[]
    words = ['A','E','I','O','U']
    word_list=[]
    for i in range(1,6):
        for j in product(words,repeat=i):temp_list.append(j)    
        
    temp_list.sort()
    for i in temp_list:
        st="".join(st)
        word_list.append(st)
    return word_list.index(word)+1