start = int(input("Пробежал 1й день"))
end = int(input("Необходимый результат"))
day = 0
res = start
while res < end:
    print(f"{day+1}-й день: {res}")
    res += res * 0.1
    day += 1
print(f"на {day+1}й день спортсмен достиг результата!")
