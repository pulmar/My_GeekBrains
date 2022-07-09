i = int(input("Введите число"))
max_num = 0
while i > 0:
    cur_num = i % 10
    i //= 10
    if cur_num > max_num:
        max_num = cur_num
    continue
print(f"Максимальное число: {max_num}")
