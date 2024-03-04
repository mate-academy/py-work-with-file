# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file, \
            open(report_file_name, "w") as report_file:
        report_dict = {}
        for line in data_file:
            op_type, amount = line.split(",")
            report_dict[op_type] = report_dict.get(op_type, 0) + int(amount)
        report_file.write(f"supply,{report_dict['supply']}\n")
        report_file.write(f"buy,{report_dict['buy']}\n")
        report_file.write(f"result,"
                          f"{report_dict['supply'] - report_dict['buy']}\n")
