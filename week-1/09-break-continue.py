# break example
num = 1
while num <= 10:
    print(num)
    if num == 5:
        break
    num += 1

# continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
