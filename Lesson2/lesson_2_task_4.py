
n = int(input("Введите число:"))


def fizz_buzz(n):
    for n in range (1,(n + 1)):
        if n % 3 == 0 and n % 5 == 0:
            print(str(n),'FizzBuzz')
        elif n % 3 == 0:
            print (str(n),'Fizz')
        elif n % 5 == 0:
           print (str(n),'Buzz') 
        else:
            print(str(n))
fizz_buzz(n)