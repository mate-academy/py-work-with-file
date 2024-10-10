import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    report_file_dict = {}

    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)

        for line in csv_reader:
            if len(line) != 2:
                continue

            operation, amount = line
            if report_file_dict.get(operation):
                report_file_dict[operation] = (
                    int(report_file_dict[operation]) + int(amount)
                )
            else:
                report_file_dict[operation] = int(amount)

    report_file_dict["result"] = (
        report_file_dict.get("supply", 0) - report_file_dict.get("buy", 0)
    )

    with open(report_file_name, "w") as report_file:
        operations_order = ["supply", "buy", "result"]
        for operation in operations_order:
            report_file.write(f"{operation},"
                              f"{report_file_dict.get(operation, 0)}\n")
