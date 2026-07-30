def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    # створили тотали, куди будемо рахувати суму
    with open(data_file_name, "r", newline="") as f:
        # відкриваємо файл для читання
        for line in f:
            line = line.strip()
            # забираємо зайві пробіли та символи переносу рядка
            if not line:
                continue
            # розділяємо рядок на частини пл комі
            parts = line.split(",")
            op = parts[0].strip()
            amt = int(parts[1].strip())
            # отримуємо операцію та кількість
            if op == "supply":
                supply_total += amt
            elif op == "buy":
                buy_total += amt
            # рахуємо тотали для кожної операції
    result = supply_total - buy_total
    with open(report_file_name, "w", newline="") as out:
        out.write(f"supply,{supply_total}\n")
        out.write(f"buy,{buy_total}\n")
        out.write(f"result,{result}\n")
        # записуємо результат у файл
