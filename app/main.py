import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    operation_amounts = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                operation_type, amount = row
                if operation_type in operation_amounts:
                    operation_amounts[operation_type] += int(amount)

    result = operation_amounts["supply"] - operation_amounts["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write("supply,{}\n".format(operation_amounts["supply"]))
        report_file.write("buy,{}\n".format(operation_amounts["buy"]))
        report_file.write("result,{}\n".format(result))
