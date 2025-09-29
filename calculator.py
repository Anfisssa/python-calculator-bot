def calculate(expression):
    """
    Принимает строку с математическим выражением, вычисляет и возвращает результат.
    Поддерживает +, -, *, /.
    """
    try:
        # Разбиваем строку на части, например "5 + 3" -> ["5", "+", "3"]
        parts = expression.split()
        if len(parts) != 3:
            return "Ошибка: Введите выражение в формате 'число оператор число' (например, 10 / 2)."

        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Ошибка: Деление на ноль невозможно!"
            return num1 / num2
        else:
            return "Ошибка: Неизвестный оператор. Используйте +, -, * или /."

    except ValueError:
        return "Ошибка: Убедитесь, что вы вводите числа."
    except Exception as e:
        return f"Произошла непредвиденная ошибка: {e}"

def main():
    """
    Главная функция для запуска калькулятора.
    """
    print("🤖 Бот-калькулятор запущен!")
    print("Введите математическое выражение (например, 5 * 3) или 'выход' для завершения.")

    while True:
        user_input = input("Ваш пример: ")

        if user_input.lower() == 'выход':
            print("Бот: До свидания!")
            break

        result = calculate(user_input)
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()
