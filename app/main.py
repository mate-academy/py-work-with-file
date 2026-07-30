import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        reader = csv.reader(data_file)
        data = list(reader)

    supply_total = 0
    buy_total = 0
    for operation, amount in data:
        if operation == "supply":
            supply_total += int(amount)
        elif operation == "buy":
            buy_total += int(amount)
    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
