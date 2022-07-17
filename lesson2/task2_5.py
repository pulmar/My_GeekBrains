my_list = [7, 5, 3, 3, 2]
num = ""

while num != "q":
  i = 0
  num = input("Введите число")

  if num.isdigit():
    for n in my_list:
       if int(num) <= n:
         i += 1
       else:
        break
    my_list.insert(i, float(num))
  print(my_list)