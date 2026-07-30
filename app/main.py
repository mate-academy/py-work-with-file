import csv


def create_report(
        data_file_name: str,
        report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue

            operation, amount = row
            if operation == "supply":
                supply_sum += int(amount)
            elif operation == "buy":
                buy_sum += int(amount)

    result = supply_sum - buy_sum

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_sum}\n")
        file.write(f"buy,{buy_sum}\n")
        file.write(f"result,{result}\n")
