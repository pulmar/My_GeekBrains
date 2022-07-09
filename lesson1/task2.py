sec = int(input("Введите время в секундах"))
h = int (sec // 3600)
m = int (sec // 60)
print(f"Время: {h}:{m%60}:{sec%60}")
