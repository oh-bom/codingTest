array=[7,5,9,0,3,1,6,2]

for i in range(1,len(array)):
    for j in range(i,0,-1): #index i시작->0끝 (-1씩)
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]

        else: #나보다 작은 애를 만났을때 종료
            break
