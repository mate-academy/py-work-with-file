import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}

    with open(data_file_name, "r", newline="") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if len(row) == 2:
                operation, amount = row
                amount = int(amount)

                if operation == "supply":
                    data["supply"] += amount
                elif operation == "buy":
                    data["buy"] += amount

    result = data["supply"] - data["buy"]
    report = f"supply,{data['supply']}\nbuy,{data['buy']}\nresult,{result}\n"

    with open(report_file_name, "w", newline="") as report_file:
        report_file.write(report)
