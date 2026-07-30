def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name, "r") as input_data, \
            open(report_file_name, "w") as report:
        for line in input_data.readlines():
            index = line.index(",")
            parameter = line[:index]
            value = line[index + 1:]
            if parameter == "supply":
                supply += int(value)
            elif parameter == "buy":
                buy += int(value)
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
