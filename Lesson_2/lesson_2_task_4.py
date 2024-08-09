def fizz_buzz(n):
    n=int(n)+1
    for y in range(1,n):
        if (y % 3 == 0) and (y % 5 != 0):
            print("Fizz")
        elif (y % 3 != 0) and (y % 5 == 0):
            print("Buzz")
        elif (y % 3 == 0) and (y % 5 == 0):
            print("FizzBuzz")
        else:
            print(y)
fizz_buzz(input("Введите число: "))