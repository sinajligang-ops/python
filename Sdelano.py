cena  = float(input("Введите сумму покупки: "))
if cena > 1000: 
    print(f"Ваша скидка 10% !!!")
if cena < 1000:
    print(f"Ваша скидка 5% !!!")
itog = cena * 0.5
print(f"Итого к оплатe: {itog:.2f} ₽")