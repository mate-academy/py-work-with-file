import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        csvreader = csv.reader(data_file)

        for row in csvreader:
            if len(row) == 2:
                type_operation, value = row
                if type_operation == "supply":
                    supply += float(value)
                elif type_operation == "buy":
                    buy += float(value)
        result = supply - buy

    with open(report_file_name, "w") as report_file:
        csvwriter = csv.writer(report_file)
        csvwriter.writerows([
            ["supply", int(supply)],
            ["buy", int(buy)],
            ["result", int(result)],
        ])
