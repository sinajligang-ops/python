correctpassword = "1234567"
userpassword = input("Введите пароль: ")
if userpassword == correctpassword:
    print("Добро пожаловать в меню!")
else: 
    print("Пароли не совпадают, осталось 3 попытки")