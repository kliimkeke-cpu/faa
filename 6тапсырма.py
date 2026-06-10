import json
import os

FILENAME = "students.json"


# Файлдан мәліметтерді оқу
def load_students():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except:
            return []
    return []


# Файлға сақтау
def save_students(students):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


# Студент қосу
def add_student(students):
    print("\n===== Студент қосу =====")

    while True:
        name = input("Аты-жөні: ").strip()
        if name:
            break
        print("Қате! Аты бос болмауы керек.")

    while True:
        try:
            age = int(input("Жасы: "))
            if age > 0:
                break
            print("Қате! Жас оң сан болуы керек.")
        except ValueError:
            print("Қате! Сан енгізіңіз.")

    while True:
        try:
            grade = float(input("Бағасы: "))
            if 0 <= grade <= 100:
                break
            print("Қате! Баға 0-100 аралығында болуы керек.")
        except ValueError:
            print("Қате! Сан енгізіңіз.")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    save_students(students)

    print("\nСтудент сәтті қосылды!")


# Студенттер тізімі
def show_students(students):
    print("\n===== Студенттер тізімі =====")

    if not students:
        print("Тізім бос.")
        return

    for i, student in enumerate(students, start=1):
        print(
            f"{i}. {student['name']} | "
            f"Жасы: {student['age']} | "
            f"Бағасы: {student['grade']}"
        )


# Статистика
def show_statistics(students):
    print("\n===== Статистика =====")

    if not students:
        print("Студенттер жоқ.")
        return

    total_students = len(students)

    average_grade = sum(s["grade"] for s in students) / total_students

    best_student = max(students, key=lambda x: x["grade"])

    print(f"\nСтуденттер саны: {total_students}")
    print(f"Орташа баға: {average_grade:.2f}")

    print("\nЕң жоғары баға:")
    print(f"{best_student['name']} - {best_student['grade']}")


# Негізгі бағдарлама
def main():
    students = load_students()

    while True:
        print("\n===== Студенттер базасы =====")
        print("1. Студент қосу")
        print("2. Студенттер тізімін көру")
        print("3. Статистика")
        print("0. Шығу")

        choice = input("\nТаңдауыңыз: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            show_students(students)

        elif choice == "3":
            show_statistics(students)

        elif choice == "0":
            print("Бағдарлама аяқталды.")
            break

        else:
            print("Қате таңдау! Қайта енгізіңіз.")


if __name__ == "__main__":
    main()