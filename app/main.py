import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue

            operation_type, amount = row[0], int(row[1])

            if operation_type == "supply":
                supply_total += amount
            elif operation_type == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, mode="w", encoding="utf-8") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")
