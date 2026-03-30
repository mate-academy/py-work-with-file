import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_1,\
         open(report_file_name, "w", newline="") as file_2:

        data_reader = csv.reader(file_1)
        data_writer = csv.writer(file_2)
        supply, buy = 0, 0

        for row in data_reader:
            if len(row) == 2:
                operation_type, amount = row
            if operation_type == "supply":
                supply += int(amount)
            if operation_type == "buy":
                buy += int(amount)

        result = supply - buy

        data_writer.writerow(["supply", supply])
        data_writer.writerow(["buy", buy])
        data_writer.writerow(["result", result])
