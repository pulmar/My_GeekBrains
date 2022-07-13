my_list = [7, 5, 3, 3, 2]
num = int(input("Введите число"))
if num in my_list:
  my_list.index(num)
  ind = my_list.index(num)
  my_list.insert(ind, num)
else:
  my_list.append(num)
print(my_list)