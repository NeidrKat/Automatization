years = int(input("Введите год:"))

def is_year_leap(years): 
    if (years % 4 == 0):
        print(True)
    else:
        print(False)
is_year_leap(years)
#------------------------------------------
years = int(input("Введите год:"))

def is_year_leap(years): 
    if (years % 4 == 0):
        print("год:", years, True)
    else:
        print("год:", years, False)
is_year_leap(years)
