import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_amount = 0
    buy_amount = 0

    with open(data_file_name, "r") as read_csv:
        data = csv.reader(read_csv)
        for operation in data:
            if operation[0] == "supply":
                supply_amount += int(operation[1])
            if operation[0] == "buy":
                buy_amount += int(operation[1])
        result = supply_amount - buy_amount

    result_operations = [
        ["supply", supply_amount],
        ["buy", buy_amount],
        ["result", result]
    ]

    with open(report_file_name, "w") as csvfile_to_write:
        csvwriter = csv.writer(csvfile_to_write)
        csvwriter.writerows(result_operations)
