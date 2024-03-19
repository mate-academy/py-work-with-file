import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    operation_totals = {"supply": 0, "buy": 0}

    with open(data_file_name, mode="r") as data_file:
        csv_reader = csv.reader(data_file)
        for row in csv_reader:
            if len(row) == 2 and row[0] in operation_totals:
                operation_totals[row[0]] += int(row[1])

    result = operation_totals["supply"] - operation_totals["buy"]

    with open(report_file_name, mode="w") as report_file:
        report_file.write("supply," + str(operation_totals["supply"]) + "\n")
        report_file.write("buy," + str(operation_totals["buy"]) + "\n")
        report_file.write("result," + f"{result}\n")
