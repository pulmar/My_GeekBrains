season_dict = {
    "зима": [12, 1, 2],
    "весна": [3, 4, 5],
    "лето": [6, 7, 8],
    "осень": [9, 10, 11],
}
month = int(input("Введите число месяца"))
for key in season_dict.keys():
      if month in season_dict[key]:
        print(key)
