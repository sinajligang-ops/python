seconds = int(input("Введите количество секунд:"))
hours = seconds // 3600
minutes_and_hours = seconds % 60
time = seconds // 60
print(f"{hours} час(ов), {minutes_and_hours} осталось секунд, {time} полных минут.")