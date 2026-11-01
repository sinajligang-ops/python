#if password == "111":
#level = input("Введите уровень доступа (1 или 2): ")
 #   if level == "2":
#        codeword = input("Введите кодовое слово: ")
#        if codeword.lower() == "админ":
#            print("Доступ к секретным файлам открыт!")
 #       else:
 #           print("Неверное кодовое слово")
#    else:
#        print("У вас обычный доступ")
#else:
#    print("Доступ закрыт")



#day, food, water, health = 1, 3, 3, 100
#while day <= 5 and health > 0:
#    print(f"День {"День"}: Здоровье {health}%, Еда {food}, Вода {water}")
#    if food < 1 or water < 1: 
#        health -= 20; print("Голод/Жажда! -20% здоровья")
#    action = input("1-Искать еду, 2-Собрать воду, 3-Отдыхать: ")
#    if action == "1": food += 1; health -= 30; print("+1 еда, -30% здоровье")
#    elif action == "2": water += 1; print("+1 вода")
#    elif action == "3": health += 20; print("+20% здоровье")
#    else: print("Пропуск хода")    
#    health -= 5; day += 1
#print("\n Игра окончена.")
#if health > 0: print("Выжил!")
#else: print("Смерть...")


#mylimit = 0
#while mylimit < 10:
#    mylimit += 1
#    print("Мне лень выводить по 10 раз")


#userWord = None
#while userWord != "stop":
#    userWord = input("Введите любое слово")
#    print(userWord)



#number = 0
#summa = 0
#while number <= 99:
#    number += 1
#    summa += number
#print(f"{number}, {summa}")



#day, food, water, health = 1, 3, 3, 100
#while day <= 5 and health > 0:
    #print(f"День {"День"}: Здоровье {health}%, Еда {food}, Вода {water}")
    #if food < 1 or water < 1: 
    #    health -= 20; print("Голод/Жажда! -20% здоровья")
    #action = input("1-Искать еду, 2-Собрать воду, 3-Отдыхать: ")
    #if action == "1": food += 1; health -= 30; print("+1 еда, -30% здоровье")
    #elif action == "2": water += 1; print("+1 вода")
    #elif action == "3": health += 20; print("+20% здоровье")
    #else: print("Пропуск хода")    
    #health -= 5; day += 1
#print("\n Игра окончена.")
#if health > 0: print("Выжил!")
#else: print("Смерть...")


#for i in range(4): 
    #print("3")


#for i in range(5):
    #print("Привет")


# for i in range(10, 0, -1):
#     print(i)
# print("Поехали")


# for i in range(8, 16):
#     print(i)



# for i in range(15):
#     robotChoice = input("товар целый ? 1 - да, 2 - нет")
#     intact = 0
#     if robotChoice == "1":
#         intact += 1
# print("Количество целых товаров равняется", intact)



# balance = 5000
# for i in range(3):
#     sum = float(input("Введите сумму для снятия"))
#     if balance >= sum:
#         balance -= sum
#         print(f"Снято {sum} рублей")
#         print(f"Оставшийся баланс: {balance} P")
#     else: 
#         print("Недостаточно средств")



# balance = 10000
# while True:
#     userSum = int(input("Введите сумму для снятия: "))
#     if userSum <= balance:
#         balance -= userSum
#         print(f"Снятие {userSum}рублей, остаток на балансе {balance} рублей")
#     elif userSum > balance:
#         print("Операция отклонена, недостаточно средств")
#     else:
#         print("Некоректные данные")
#     userChoice = input("Хотите завершитm ? 1 - да, 2 - нет: ")
#     if userChoice == "1":
#         print("Всего доброго")
#         break



# while True:
#     userWord = input("Введи любое слово и выведу в консоль, или напиши 'stop':")
#     if userWord == "stop":
#         break
#     else: 
#         print(userWord)



# for i in range(10):
#     if i == 2 or i == 8:
#         continue
#     print(i)



# items = 0
# while True:
#     userItems = input("Что положим в рюкзак ? Если хочешь закончить, напиши 0")
#     if userItems == "Стекло":
#         print("Стекло нельзя")
#         continue
#     elif userItems == "0":
#         break 
#     else:
#         items += 1 
# print(f"Вы набрали {items} вещей")


# items = "предмет"
# for i in range(7):
#     userItems = input("Что ты хочешь положить в посылку ?")
#     if userItems == "стекло":
#         print("Стекло нельзя, опасно !")
#         continue
#     else: 
#         print(f"{items} добавлен в коробку")
# print(f"Посылка собрана и готова к отправке")



# import time 
# for i in range (10, 0, -1):
#     print(i)
#     time.sleep(1)



# for i in range(1, 11):
#     print (i, end = "")



# import time
# for i in range(10,0,-1):
#     for j in range(10,1,-1):
#         print(f"\r{i}:{j}", end = "")
#         time.sleep(1)
#     print("Прошло 10 секунд")
# print("Время пришло")


# for i in range(10):
#     for j in range(i):
#         print("*", end = "")
#     print()


# n = 5
# for i in range(n):
#     print(' ' * (n - i - 1), end='')
#     print('*' * (2*i + 1))
# for i in range(n-2, -1, -1):
#     print(' ' * (n - i - 1), end='')
#     print('*' * (2*i + 1))




# userChoice = input("Здраствуй хозяин, выберите, какую функцию мне выполнить, 1 - начать минутную уборку, 2 - вернуться на зарядку, 3 - покатать кота под музыку : ")
# if userChoice == "1":
#     print("Принято, начинаю 10 минутную (точнее 60 секундную) уборку")
#     import time
#     for i in range(60, 0, -1):
#         for j in range(1, 0, -1):
#             print(f"\r{i}:{j}", end = "")
#             time.sleep(0)
#         print("Время пришло")
# if userChoice == "2":
#     print("Принято, возвращаюсь на зарядку")
# elif userChoice == "3":
#     print("Принято хозяин, начинаю катать кота под веселую музыку 30 cекунд")
#     import time
#     for i in range(30, 0, -1):
#         for j in range(1, 0, -1):
#             print(f"\r{i}:{j}", end = "")
#             time.sleep(1)
#     print(" Время пришло, возвращаюсь на зарядку...")
# else: 
#     print("Некорректые данные")
    


# def getSquare(a, b):
#     square = a + b
#     return square


# print('Площадь прямоугольника', getSquare(5, 7))
# print('Площадь прямоугольника', getSquare(8, 4))
# print('Площадь прямоугольника', getSquare(12, 9))



# def convert(rub):
#     dollar_Cours = 86
#     dollars = rub / dollar_Cours
#     return f"вы получите {dollars:.2f} долларов "


# def convert2(rub):
#     euro_Cours = 100 
#     euro = rub / euro_Cours
#     return f"вы получитe {euro:.2f} евро"

# print("Курс евро в рублях", convert2(200))
# print("Курс евро в рублях", convert2(5000))
# print("Курс доллара", convert(10000))
# print("Курс доллара", convert(6000))




# def Delivery(sum, distance):
#     sum = float(input("Введите сумму заказа: "))
#     distance = float(input("Введите растояние: "))
#     if sum > 2000:
#         result = str("Доставка бесплатно")
#     elif 0 < distance < 5:
#         result = str("За доставку c вас 200 р.")
#     elif 5 <= distance <= 20:
#         result = str("За доставку c вас 500 р.")
#     return result


# def calculate_tax(salary):
#     if salary < 50000:
#         return salary * 0.13
#     else:
#         return salary * 0.15
# def get_net_salary(salary):
#     tax = calculate_tax(salary)
#     return salary - tax
# salary = float(input("Введите зарплату: "))
# tax = calculate_tax(salary)
# net = get_net_salary(salary)
# print("Налог:", tax, "На руки:", net)


# def someFunction():
#     someVariable = 5

# def moreFunction():
#     someVariable = 5
#     result = someVariable
#     return result

# print(someVariable)
# print(moreFunction())


# count = 0
# ....
# ....
# ....
# ....
# ....


# def increaseCount():
#     global count 
#     count + 1
#     return count

# budget = 5000
# def spend(amount):
#     global budget
#     budget -= amount
#     return f"Потрачено {amount} рублей, осталось {budget:.2f}"
# print(spend(3239))

# password = "12345"
# def checkPassword(input_pass):
#     secret = "12345"
#     password = "12345"
#     input("Введите пароль")
#     if secret == password:
#         print("Добро пожаловать")
#     else:
#         print("Пароль не верный !☠️")


# total_km = 0
# def log_run(km):
#     global total_km
#     total_km += km
#     return f"Пробежали сегодня: {km} км"
# def show_progress():
#     return f"Всего пробежано: {total_km} км"
# print(log_run(3))
# print(log_run(5))
# print(log_run(2))
# print(show_progress())


# def factorial(n):
#     if n == 0:
#         return 1
#     else: 
#         return n * factorial(n - 1) 
    
# print(factorial(5))


# import time 

# for i in range(3):
#     print("Прошло 2 секунды")
#     time.sleep(2)


# from datetime import datetime, timedelta
# user_days = int(input("Через сколько дней событие: "))
# today = datetime.now()
# event_date = today + timedelta(days=user_days)
# print(f"Событие состоится: {event_date.strftime('%d.%m.%Y')}")

# import time
# start = time.time()
# for _ in range(5000000):
#     pass
# end = time.time()

# print(f"Выполнение заняло: {end - start:.4f} секунд")

# from datetime import datetime, timedelta
# user_days = 0
# today = datetime.now()
# event_date = today + timedelta(days=user_days)
# print(f"Cегодня: {event_date.strftime('%d.%m.%Y')}")


# names = []
# names = ["Иван", "Роберт", "Артем", "Катя", "Максим"]
# numbers = [1, 2, 3, 4, 5]
# print(names)
# print(names[1])
# print(names[1:3])
# print(numbers[::3])

# for i in range(len(numbers)):
#     if numbers[i] == 7:
#         print(numbers[i])

# if "Артем" in names:
#     print("Человек найден")

# names.append("Витя")
# print(names)
# names.remove("Катя")


# names.pop("Максим")
# print.names("Максим") 


# guests = []

# for i in range(5):
#     name = input("Введите имена гостей: ")
#     guests.append(name)
# later = input("Опоздал: ")
# if later in guests: 
#     guests.remove(later)
#     print(later, "опоздал(удален из списка)")
# else: 
#     print(later, "не приглашен")
# print("Итоговый список приглашенных:", guests)



# scores = [5, 2, 9, 2]
# scores.sort()
# print(2 in scores)
# print(scores.count(2))

# fruits = ["яблоко", "груша", "слива "]
# for i, item in enumerate(fruits):
#     print(f"{i}: {item}")


# nums = [1, 2, 3, 4, 5]
# new_nums = []
# for n in nums:
#     if n % 2 == 0:
#         new_nums.append(n * 2)
# print(new_nums)


# numbers = [3, 7, 12, 5, 9]
# for i in numbers: 
#     print(i * 2)
# total = sum(numbers)
# print("Сумма всех чисел:", total)


# temps = [12, 15, 18, 14, 20, 22, 19]
# print(min(temps))
# print(max(temps))
# print(f"(sum(temps)/7:.0f")
# temps_sum = sum(temps)
# middle_temps = temps_sum/len(temps)
# print(temps)


# days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# print(days[0:5])
# days[5] = "Выходной"
# days[6] = "Выходной"
# days.reverse
# print(days)


#products = {'Кастрюля': 500, 'Тарелка': 300, 'Ноутбук': 100000, 'Наушники': 5000, 'Зарядник': 2000}


# product = [
#     {
#         'productName': 'Ноутбук',
#         'price': 100000
#     },
#     {
#     'productName': 'Телефон',
#     'price': 50000
#     },
#     {
#         'productName': 'Планшет',
#         'price': 70000,
#     }
# ]

# phone = {
#     'productName': 'Самсунг Гелакси S26 ультра',
#     'price': 100000
# }
# phone['price'] = 120000
# print(phone)
# phone['color'] = "Черный"
# print(phone)

# if "color" in phone:
#     print(phone['color'])
#     del phone["color"]

# student = {
#     'name': 'Артем', 
#     'grade': 4,
#     'subject': 'Математика',
# }
# print(student['name'], student['grade'], student['subject'])
# student['grade'] = 5
# print(student)
# student['homework_done'] = True
# print(student)

# numberPhones = {
#     'Anna': '123',
#     'Ivan': '456'
# }
# numberPhones['Anna'] = 999
# print(numberPhones)
# numberPhones['Maria'] = 789
# print(numberPhones)
# if "numberphones" in numberPhones:
#     print(numberPhones['Petr'])
#     del numberPhones["Petr"]
# else: 
#     print("человек не найден")
# print(numberPhones)


# product = {'title': 'Ноутбук', 'price': 50000, 'discount': 10}
# product['final_price'] = product['price'] * (100 - product['discount']) / 100
# print(product)


# info = {
#     'Name': 'Александр',
#     'Age': 21,
#     'City': 'Брянск',
#     'Hobby': 'Програмирование',
# }
# print(info['Name'], info['Age'], info['City'], info['Hobby'])
# info['Сity'] = 'Update: Санкт - Питербург'
# print(info)

# scores = {'Math': 95,
#         'English': 82,
#         'Code': 100
# }
# for subject, points in scores.items():
#     print(f'{subject}: {points} ')
# for point in scores.values():
#     if points > max_points:
#         max_point = points
# print(f"Максимальный бал: {points}")


# shop = {"apple":50, "banana":30, "cherry":80}
# shop1 = {}
# for subject, points in shop. items():
#     shop1[subject] = points * (80/100) 
#     print(f"{subject}: {points}")
# print (shop1) 

# grades = {'Ivan': [4, 5, 4], 'Anna': [5, 5, 5], 'Petr': [3, 4, 4]}
# for name, marks in grades.items():
#     average = sum(marks) / len(marks)
#     if average >= 4.5:
#         print(name)


prices = {'Хлеб': [40, 45, 42], 'Молоко': [80, 85, 90], 'Сыр': [300, 310, 320], 'Яблоки': [100, 95, 105]}
for name, values in prices.items():
    average = round(sum(values)) / round(len(values), 2)
    print(name, "-", average)
    if average < 100:
        print("Дешевый товар:", name)

# grades = {'Ivan': [4, 5, 4], 'Anna': [5, 5, 5], 'Petr': [3, 4, 4]}
# for name, marks in grades.items():
#     average = sum(marks) / len(marks)
#     if average >= 4.5:
#         print(name)