import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            action_type, count = row[0].strip(), int(row[1].strip())
            if action_type == "supply":
                supply_total += count
            elif action_type == "buy":
                buy_total += count

    result = supply_total - buy_total

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")
