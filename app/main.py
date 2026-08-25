import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            operation_type, amount = row[0].strip(), int(row[1].strip())
            if operation_type == "supply":
                supply += amount
            elif operation_type == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
