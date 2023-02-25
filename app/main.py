def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}
    with open(data_file_name) as data, open(report_file_name, "a") as report:
        for line in data.readlines():
            operation, value = line.strip().split(",")
            report_dict[operation] += int(value)
        for operation in report_dict:
            report.write(f"{operation},{report_dict[operation]}\n")
        report.write(
            f"result,{report_dict['supply'] - report_dict['buy']}\n"
        )
