import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    reader = csv.reader(data_file)
    supply_total = 0
    buy_total = 0
    for row in reader:
        if not row:
            continue
        operation, amount = row[0], int(row[1])
        if operation == "supply":
            supply_total += amount
        elif operation == "buy":
            buy_total += amount
    data_file.close()
    file_report = open(report_file_name, "w")
    file_report.write(f"supply,{supply_total}\n")
    file_report.write(f"buy,{buy_total}\n")
    file_report.write(f"result,{supply_total - buy_total}\n")
    file_report.close()
