x = int(input("Введите сумму вклада:"))
y = int(input("На какое количество лет хотите сделать вклад?:"))

def bank():
    procent = 0.1
    sum_after_years = x * (1 + procent) ** y 
    print("Ваш расчет:", round(sum_after_years))
bank()
