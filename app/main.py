def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}
    with open(data_file_name) as data:
        for line in data.readlines():
            operation, num = line.strip("\n").split(",")
            if operation in result:
                result[operation] += int(num)
            else:
                result[operation] = int(num)
    with open(report_file_name, "w") as report:
        report.write(f"supply,{result['supply']}\n")
        report.write(f"buy,{result['buy']}\n")
        report.write(f"result,{result['supply'] - result['buy']}\n")
