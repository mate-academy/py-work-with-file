def create_report(data_file_name: str, report_file_name: str):

    report_dict = {}

    with open(data_file_name, "r") as main:
        for line in main.readlines():
            operation_type, amount = line.split(",")
            if operation_type not in report_dict:
                report_dict[operation_type] = int(amount)
            else:
                report_dict[operation_type] += int(amount)

    with open(report_file_name, "w") as report:
        result = f"supply,{report_dict['supply']}\n" \
                 f"buy,{report_dict['buy']}\n" \
                 f"result,{report_dict['supply'] - report_dict['buy']}\n"

        report.write(result)
