#side1 = float(input("Введите сторону a: "))
#side2 = float(input("Введите сторону b: "))
#side3 = float(input("Введите сторону c: "))
#if side1 > 0 and side2 > 0 and side3 > 0 and (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
#    print("Треугольник существует")
#else:
#   print("Треугольник не существует")



userChoise = input("Что вы будете, 1 - бургер, 2 - пиццу ?: ")
if userChoise == "1": 
    cheese = input("Добавить сыр ? 1 - да, 2 - нет")
    if cheese == "1":
        print("Начали готовить чизбурер")
    elif cheese == "2": 
        print("начали готовить гамбургер")
elif userChoise == "2":
    choose = input("Какую пиццу хотите, 1 - сырную, 2 - пеперони, 3 - охотничая : ")
    if choose == "1":
        print("Начали готовить сырную пиццу")
    if choose == "2":
        print("Начали готовить пиццу пеперони")