#https://school.programmers.co.kr/learn/courses/30/lessons/67256?language=python3

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand="right"

def find_location(number):
    if number==0:
        row=3
        column=1
    else:
        row=(number-1)//3
        column=(number-1)%3

    return row,column

def clostest(tx,ty,left,right):
    lx,ly=left
    rx,ry=right
 
    ldif=abs(lx-tx)+abs(ly-ty)
    rdif=abs(rx-tx)+abs(ry-ty)
    
    if ldif>rdif:
        return "R"
    elif ldif==rdif:return "S"
    else:return "L"

def solution(numbers, hand):
    board=[[0]*3 for _ in range(4)]
    left=[3,0]
    right=[3,2]

    #한번에 할당하는거 찾아보기
    # for i in range(3):
    #     for j in range(3):
    #         board[i][j]=i*3+j+1
    for i in range(1,10):
        board[(i-1)//3][(i-1)%3]=i
    result = ''
    
    for number in numbers:
        x,y=find_location(number)
        
        if y==0:    
            result+="L"
            left=[x,y]
        elif y==2:
            result+="R"
            right=[x,y]
        else:
            temp=clostest(x,y,left,right)
            if temp=="S":
                if hand=="right":
                    result+="R"
                    right=[x,y]
                elif hand=="left":
                    result+="L"
                    left=[x,y]
            
            else:
                result+=temp
                if temp=="L":left=[x,y]
                elif temp=="R":right=[x,y]
       
    return result

print(solution(numbers,hand))