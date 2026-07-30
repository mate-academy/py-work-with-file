def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0}

    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):

        for line in data_file:
            data = line.split(",")

            operation_type = data[0]
            amount = data[1]

            report[operation_type] += int(amount)

        report["result"] = report["supply"] - report["buy"]

        report_file.writelines(
            f"{operation_type},{amount}\n"
            for operation_type, amount in report.items()
        )
