import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)

        for row in csv_reader:
            if row:
                operation_type, amount = row
                amount = int(amount)

                if operation_type in data_dict:
                    data_dict[operation_type] += amount

    result = data_dict["supply"] - data_dict["buy"]
    report = (
        f"supply,{data_dict['supply']}\n"
        f"buy,{data_dict['buy']}\n"
        f"result,{result}\n"
    )

    with open(report_file_name, "w", newline="") as report_file:
        report_file.write(report)
