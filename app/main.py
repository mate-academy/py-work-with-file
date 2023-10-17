def create_report(data_file_name: str, report_file_name: str) -> None:
    reports = {}

    with open(data_file_name, "r") as file:
        for line in file.readlines():
            operation_type, amount = line.split(",")
            amount = int(amount)
            if operation_type not in reports:
                reports[operation_type] = amount
            else:
                reports[operation_type] += amount
    with open(report_file_name, "w") as file:
        file.write(f"supply,{reports['supply']}\n")
        file.write(f"buy,{reports['buy']}\n")
        file.write(f"result,{reports['supply'] - reports['buy']}\n")
