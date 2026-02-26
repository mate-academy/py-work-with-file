import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r"
              ) as data_input, open(report_file_name, "w") as data_output:
        supply = 0
        buy = 0
        result = 0
        for line in data_input.readlines():
            operation, amount = line.strip().split(",")
            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)
            else:
                raise ValueError("Wrong data provided")
        result = supply - buy
        writer = csv.writer(data_output)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
