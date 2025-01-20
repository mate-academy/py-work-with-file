def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as read_file:
        # next(read_file)

        report = {}
        for line in read_file:
            operation_type, amount = line.split(",")
            amount = int(amount)
            report[operation_type] = report.get(operation_type, 0) + amount

        report["result"] = report.get("supply", 0) - report.get("buy", 0)

    with open(report_file_name, "w") as write_file:
        write_file.write("supply," + str(report.get("supply", 0)) + "\n")
        write_file.write("buy," + str(report.get("buy", 0)) + "\n")
        write_file.write("result," + str(report["result"]) + "\n")
