def create_report(data_file_name: str, report_file_name: str) -> None:
    report_buffer = {"supply": 0, "buy": 0, "result": 0}

    with open(data_file_name) as data_file:
        for row in data_file.readlines():
            row_value_list = row.strip().split(",")
            report_buffer[row_value_list[0]] += int(row_value_list[1])

        report_buffer["result"] = report_buffer["supply"] - report_buffer[
            "buy"]

    with open(report_file_name, "a") as report_file:
        for key, value in report_buffer.items():
            report_file.write(key + "," + str(value) + "\n")
