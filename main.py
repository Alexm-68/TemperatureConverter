def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp = float(input("Введите температуру: "))
unit = input("Введите единицу измерения (C/F): ").upper()

if unit == 'C':
    print(f"Температура в Фаренгейтах: {celsius_to_fahrenheit(temp):.2f}")
elif unit == 'F':
    print(f"Температура в Цельсиях: {fahrenheit_to_celsius(temp):.2f}")
else:
    print("Неверная единица измерения")


