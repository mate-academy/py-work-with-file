def create_report(data_file_name: str, report_file_name: str) -> None:
    report_data = dict()
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as report_file):
        for line in file_in.readlines():
            operation_type, amount = line.rstrip().split(",")
            if report_data.get(operation_type):
                report_data[operation_type] += int(amount)
            else:
                report_data[operation_type] = int(amount)

        result = report_data["supply"] - report_data["buy"]

        report_file.write(f"supply,{str(report_data['supply'])}\n")
        report_file.write(f"buy,{str(report_data['buy'])}\n")
        report_file.write(f"result,{result}\n")
