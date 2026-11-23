def create_report(data_file_name: str, report_file_name: str) -> None:
    """Tworzy raport podsumuwujacy operacje na podstawie pliku CSV"""

    supply_sum = 0
    buy_sum = 0
    with open(data_file_name, "r", encoding="utf-8") as file:
        for line in file:
            cleaner_line = line.strip()
            if not cleaner_line:
                continue
            part = cleaner_line.split(",")
            name = part[0]
            amount = int(part[1])

            if name == "supply":
                supply_sum += amount
            elif name == "buy":
                buy_sum += amount

    result = supply_sum - buy_sum

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{supply_sum}\n")
        file.write(f"buy,{buy_sum}\n")
        file.write(f"result,{result}\n")
