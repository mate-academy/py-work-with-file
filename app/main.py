import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                operation_type = row[0]
                amount = int(row[1])
                if operation_type == "supply":
                    total_supply += amount
                elif operation_type == "buy":
                    total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, mode="w", encoding="utf-8") as file:
        file.write(f"supply,{total_supply}\n")
        file.write(f"buy,{total_buy}\n")
        file.write(f"result,{result}\n")
