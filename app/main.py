def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        supply = 0
        buy = 0
        for line in data_file:
            if line:
                operation_type, amount = line.split(",")
                if operation_type == "supply":
                    supply += int(amount)
                if operation_type == "buy":
                    buy += int(amount)
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")
