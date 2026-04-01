def create_report(data_file_name: str, report_file_name: str) -> bool:
    if data_file_name and report_file_name:
        reports = {"supply": 0, "buy": 0}

        try:
            with open(data_file_name) as data_file:
                for line in data_file:
                    operation_type, amount = line.split(",")
                    reports[operation_type] += int(amount)
        except (FileNotFoundError, PermissionError):
            return False

        with open(report_file_name, "a+") as report_file:
            for operation_type in reports:
                report_file.write(
                    f"{operation_type},{reports[operation_type]}\n"
                )
            report_file.write(f"result,{reports['supply'] - reports['buy']}\n")
        return True
    return False
