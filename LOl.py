#else:
#    print("некорректные данные")



people = input("Являетесь ли вы военным, 1 - да, 2 - нет ")
age = int(input("Укажите ваш возвраст: "))

if people == "1":
    print("До пенсии осталось: ", 40 - age)
elif people == "2":
    gender = input("укажите ваш пол, 1 - мужчина, 2 - женщина")
    if gender == "1": 
        print("До пенсии осталось: ", 65 - age)
    elif gender == "2":
        print("До пенсии осталось: ", 60 - age)
else: 
    print("Некоректные данные")

    