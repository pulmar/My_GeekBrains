# _finance = выручка, _spend = издержки
# _itog = финансовый результат
# _rent = рентабельность
#_num_employee = число сотрудников, _itog_employee = прибыль в рассчете на 1 сотрудника

_finance = int(input("Выручка"))
_spend = int(input("Издержки"))
_itog = _finance - _spend
if _finance > _spend:
    print("Ура! Положительное сальдо")
    _rent = int((_itog / _finance) * 100)
    print(f"Рентабельность {_rent}%")
else:
    print("Отрицательное сальдо")
if _finance == _spend:
    print("Вы вышли в 0")
    _rent = (_itog / _finance) * 100
    print(f"Рентабельность {_rent}%")
_num_employee = int(input("Число сотрудников"))
_itog_employee = _itog / _num_employee
print(_itog_employee)


