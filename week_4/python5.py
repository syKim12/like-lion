import random
import time

menu = []
cnt = 0
index = random.randint(0, 4)

print("메뉴 5개 중에서 추천해드려요!")

while True:
    name = input("메뉴를 알려주세요:  ")
    for k in menu:
        if name == k:
            print("이미 있는 메뉴예요! 다른걸 알려주세요")
            menu.remove(k)
            cnt -= 1
            continue
    menu.append(name)
    cnt += 1
    print(cnt)
    if cnt == 5:
        print("5개를 모두 입력하셨어요!")
        break
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print_num = index+1
print("오늘의 메뉴는 " + str(print_num) + "번째 메뉴, " + menu[index] + "입니다!")