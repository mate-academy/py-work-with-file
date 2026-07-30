def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    report_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file:
        for line in data_file.readlines():
            if line != "":
                report_dict[line.split(",")[0]] += int(line.split(",")[1])

    with open(report_file_name, "w") as report_file:
        for key, value in report_dict.items():
            report_file.write(f"{key},{value}\n")
        report_file.write(f"result,"
                          f"{report_dict['supply'] - report_dict['buy']}\n")
