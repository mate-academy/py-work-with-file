import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as csv_data_file, \
            open(report_file_name, "a", newline="") as csv_report_file:
        data_file = csv.reader(csv_data_file, delimiter=",")
        supply_total = 0
        buy_total = 0
        for operation in data_file:
            if operation[0] == "supply":
                supply_total += int(operation[1])
            if operation[0] == "buy":
                buy_total += int(operation[1])
        result = supply_total - buy_total
        report_file = csv.writer(csv_report_file, delimiter=",")
        report_file.writerow(["supply", f"{supply_total}"])
        report_file.writerow(["buy", f"{buy_total}"])
        report_file.writerow(["result", f"{result}"])
