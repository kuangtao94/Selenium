n = 1
sum = 0
while n <= 100:
    if n %2 == 0:
        n += 1
        continue
    sum = sum + n
    n += 1
print(sum)


while True:
    name = input("请输入：")
    if name == "stop":
        break
    else:
        print(name)