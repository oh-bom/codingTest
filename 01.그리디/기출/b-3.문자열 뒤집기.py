data=input()

cnt0=0
cnt1=0

for i in range(len(data)-1):
    if(data[i]!=data[i+1] and data[i]=="0"):cnt0+=1
    elif(data[i]!=data[i+1] and data[i]=="1"):cnt1+=1

print(min(cnt0,cnt1))
    