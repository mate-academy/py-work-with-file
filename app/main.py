import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    sup = 0
    buy = 0

    with open(data_file_name, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            operation, amount = row[0], int(row[1])
            if operation == "supply":
                sup += amount
            elif operation == "buy":
                buy += amount

    with open(report_file_name, "w") as f:
        f.write(f"supply,{sup}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{sup - buy}\n")
