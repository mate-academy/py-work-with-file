def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data:
        for operation in data.read().split():
            if "supply" in operation:
                supply += int(operation.split(',')[1])
            if "buy" in operation:
                buy += int(operation.split(',')[1])
        with open(report_file_name, "w") as report:
            report.write(f"supply,{supply}\n"
                         f"buy,{buy}\n"
                         f"result,{supply - buy}\n")
