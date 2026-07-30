def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    try:
        with open(data_file_name, "r", encoding="utf-8") as f:
            for line in f:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue

                # Розбиваємо рядок за комою
                operation, amount = cleaned_line.split(",")

                if operation == "supply":
                    supply_total += int(amount)
                elif operation == "buy":
                    buy_total += int(amount)

        # Обчислюємо фінальний результат
        result = supply_total - buy_total

        # Формуємо вміст звіту
        report_content = [
            f"supply,{supply_total}",
            f"buy,{buy_total}",
            f"result,{result}"
        ]

        # Записуємо звіт у новий файл
        with open(report_file_name, "w", encoding="utf-8") as f_report:
            f_report.write("\n".join(report_content) + "\n")

    except FileNotFoundError:
        pass
