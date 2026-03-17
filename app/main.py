import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue

            operation_type, amount = row
            if operation_type == "supply":
                supply += int(amount)
            elif operation_type == "buy":
                buy += int(amount)

    result = supply - buy

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
