import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r", newline="") as data_file:
        csv_reader = csv.reader(data_file)

        for row in csv_reader:
            if row:
                operation_type = row[0]
                amount = int(row[1])

            if operation_type in totals:
                totals[operation_type] += amount

    with open(report_file_name, "w", newline="") as report_file:
        csv_writer = csv.writer(report_file)

        for operation_type, total_amount in totals.items():
            csv_writer.writerow([operation_type, total_amount])

        result = totals["supply"] - totals["buy"]
        csv_writer.writerow(["result", result])
