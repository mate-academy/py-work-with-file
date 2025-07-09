def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Створює звіт на основі даних з CSV файлу.

    Args:
        data_file_name (str): Назва файлу з вхідними даними
        report_file_name (str): Назва файлу для збереження звіту
    """
    # Змінні для зберігання сум
    total_supply = 0  # Загальна сума поставок
    total_buy = 0  # Загальна сума покупок

    # Читаємо дані з файлу
    with open(data_file_name, 'r', encoding='utf-8') as file:
        for line in file:
            # Видаляємо пробіли та символи нового рядка
            line = line.strip()

            # Пропускаємо пусті рядки
            if not line:
                continue

            # Розділяємо рядок на частини (операція, сума)
            parts = line.split(',')

            # Перевіряємо, чи є достатньо даних у рядку
            if len(parts) >= 2:
                operation_type = parts[0].strip()  # Тип операції
                amount = int(parts[1].strip())  # Сума

                # Додаємо до відповідної категорії
                if operation_type == 'supply':
                    total_supply += amount
                elif operation_type == 'buy':
                    total_buy += amount

    # Обчислюємо результат
    result = total_supply - total_buy

    # Записуємо звіт у файл
    with open(report_file_name, 'w', encoding='utf-8') as file:
        file.write(f"supply,{total_supply}\n")
        file.write(f"buy,{total_buy}\n")
        file.write(f"result,{result}\n")


# Приклад використання:
if __name__ == "__main__":
    # Створюємо тестовий файл з даними
    test_data = """supply,30
buy,10
buy,13
supply,17
buy,10
"""

    with open('test_data.csv', 'w', encoding='utf-8') as f:
        f.write(test_data)

    # Викликаємо нашу функцію
    create_report('test_data.csv', 'report.csv')

    # Читаємо та виводимо результат
    print("Звіт створено! Вміст файлу report.csv:")
    with open('report.csv', 'r', encoding='utf-8') as f:
        print(f.read())
