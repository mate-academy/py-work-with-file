import csv


def create_report(data_file_name: str,
                  report_file_name: str) -> globals():
    operations = {"supply": 0, "buy": 0}

    with open(data_file_name, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                operation, amount = row
                if operation in operations:
                    operations[operation] += int(amount)

    with open(report_file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", operations["supply"]])
        writer.writerow(["buy", operations["buy"]])
        writer.writerow(["result", operations["supply"] - operations["buy"]])
