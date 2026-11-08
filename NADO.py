#summa = float(input("Введите сумму заказа: "))
#rastoyanie = float(input("Введите расстояние(км): "))
#if summa > 2000: 
#   print(f"Доставка бесплатно")
#elif rastoyanie < 5:
#    print(f"Доставка стоит 200 рублей")
#elif 5 <= rastoyanie <= 20:
#    print(f"Доставка стоит 500 рублей")
#else:
#    if rastoyanie > 20:
#      print("Доставка не осуществляется")


#userAge = int(input("Сколько вам полных лет ? "))
#driverLisence = input("Есть ли у вас водительские права ?: ")
#if userAge >= 18 and driverLisence == "Да":
#    print("Добро пожаловать")
#elif userAge < 18 or driverLisence != "Да":
#    print("Ждем вас с водительскими правами !")
#else: 
#    print("Некоректные данные")



userType = input("1 - вы хозяин амбара, 2 - вы мышь: ")
hole1 = input("щель закрыта? да/нет: ")
hole2 = input("щель закрыта? да/нет: ")
hole3 = input("щель закрыта? да/нет: ")

if userType == "1" and hole1 == "да" and hole2 == "да" and hole3 == "да":
    print("Разочарованные мыши ушли искать теплое место в другом амбаре")
if userType == "нет" and hole1 == "нет" and hole2 == "нет" and hole3 == "нет":
    print("Мыши залезли в амбар")