import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as s, open(report_file_name, "w") as r:
        csvreader = csv.reader(s)
        supply_total = 0
        buy_total = 0

        for row in csvreader:
            operation_type, amount = row
            if operation_type == "supply":
                supply_total += int(amount)
            elif operation_type == "buy":
                buy_total += int(amount)

        result = supply_total - buy_total

        r.write(f"supply,{supply_total}\n")
        r.write(f"buy,{buy_total}\n")
        r.write(f"result,{result}\n")
