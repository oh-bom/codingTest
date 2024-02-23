n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x #target>=x

# 만들 수 없는 금액 출력
print(target)


'''
https://www.notion.so/ohbom/b-4-eb75c01d4c6c4b7ebf723dec62d1c3ec

'''
