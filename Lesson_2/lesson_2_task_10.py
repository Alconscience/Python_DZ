def bank(x,y):
    x=int(x)
    y=int(y)
    for i in range(1,y+1):
        p=x*0.1
        x=x+p
    print("Ваш вклад через",y,"лет составит:",x)
bank(input("Вклад: "),input("Срок: "))
