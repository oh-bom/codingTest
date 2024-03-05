s=str(input())
result=[]
nums=0
for x in s:
    if x.isalpha():
        result.append(x)
    else:
        nums+=int(x)

result.sort()
result.append(str(nums))
str_result="".join(result)
print(str_result)
    
'''
K1KA5CB7
'''