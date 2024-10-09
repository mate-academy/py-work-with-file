import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)
    report_file = open(report_file_name, "w")

    csv_reader = csv.reader(data_file)

    report_file_dict = {}
    for line in csv_reader:

        operation, amount = line
        if report_file_dict.get(operation):
            report_file_dict[operation] = (
                int(report_file_dict[operation]) + int(amount)
            )
        else:
            report_file_dict[operation] = amount
    report_file_dict["result"] = (
        report_file_dict["supply"] - report_file_dict["buy"]
    )

    operations_order = ["supply", "buy", "result"]
    for operation in operations_order:
        report_file.write(f"{operation},{report_file_dict[operation]}\n")
