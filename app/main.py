import csv


def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    operation_sums = {"supply": 0, "buy": 0}

    with open(data_file_name, mode="r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                operation_type, amount = row
                amount = int(amount)
                if operation_type in operation_sums:
                    operation_sums[operation_type] += amount

    result = operation_sums["supply"] - operation_sums["buy"]

    with open(report_file_name, mode="w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["supply", operation_sums["supply"]])
        csv_writer.writerow(["buy", operation_sums["buy"]])
        csv_writer.writerow(["result", result])
