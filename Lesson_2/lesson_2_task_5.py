def month_to_season(m):
    m=int(m)
    if (m<1) or (m>12):
        print("Неправильно введен номер месяца")
    elif (m==12) or (m==1) or (m==2):
        print("Зима")
    elif (m==3) or (m==4) or (m==5):
        print("Весна")
    elif (m==6) or (m==7) or (m==8):
        print("Лето")
    else:
        print("Осень")
month_to_season(input("Номер месяца - "))