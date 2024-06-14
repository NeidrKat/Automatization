
m = int(input("Введите номер месяца:"))

def month_to_season(m):
    if (m == 12) or (m == 1) or (m == 2):
        print("зима")
    if (m == 3) or (m == 4) or (m == 5):
        print("весна")
    if (m == 6) or (m == 7) or (m == 8):
        print("лето")
    if (m == 9) or (m == 10) or (m == 11):
        print("осень")
month_to_season(m)
    
    