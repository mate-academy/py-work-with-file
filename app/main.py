def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    report = {}
    with open(data_file_name, "r") as old_file:
        for line in old_file.readlines():
            line_ls = line.split(",")
            if line_ls[0] not in report:
                report[line_ls[0]] = line_ls[1]
            else:
                report[line_ls[0]] += line_ls[1]
    with open(report_file_name, "w") as new_file:
        for data in report:
            new_file.write(f"{data},{report[data]}\n")
