n=str(input())

left=0
right=0
half=len(n)//2
for i in range(half):
    left+=int(n[i])
for i in range(half,len(n)):
    right+=int(n[i])

if left==right:print("LUCKY")
else:print("READY")

