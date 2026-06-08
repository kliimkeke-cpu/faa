from datetime import datetime

count = 0

while True:
    print("\n===== Конвертер =====")
    print("1. Км -> М")
    print("2. М -> Км")
    print("3. Кг -> Г")
    print("4. Г -> Кг")
    print("5. C -> F")
    print("6. F -> C")
    print("0. Шығу")

    choice = input("\nТаңдау: ")

    if choice == "0":
        print("\nБағдарлама аяқталды.")
        print(f"Жалпы орындалған конвертация саны: {count}")
        break

    elif choice == "1":
        km = float(input("Км енгізіңіз: "))
        result = km * 1000
        print(f"{km} км = {result} м")
        count += 1

    elif choice == "2":
        m = float(input("М енгізіңіз: "))
        result = m / 1000
        print(f"{m} м = {result} км")
        count += 1

    elif choice == "3":
        kg = float(input("Кг енгізіңіз: "))
        result = kg * 1000
        print(f"{kg} кг = {result} г")
        count += 1

    elif choice == "4":
        g = float(input("Г енгізіңіз: "))
        result = g / 1000
        print(f"{g} г = {result} кг")
        count += 1

    elif choice == "5":
        c = float(input("°C енгізіңіз: "))
        result = (c * 9 / 5) + 32
        print(f"{c}°C = {result}°F")
        count += 1

    elif choice == "6":
        f = float(input("°F енгізіңіз: "))
        result = (f - 32) * 5 / 9
        print(f"{f}°F = {result:.2f}°C")
        count += 1

    else:
        print("Қате таңдау!")
        continue

    print("\nКонвертация сәтті аяқталды")
    print("Уақыты:")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print(f"\nЖалпы орындалған конвертация саны: {count}")