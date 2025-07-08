def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {}
    with open(data_file_name, "r") as data:
        lines = []
        for line in data.readlines():
            lines.append(line.rstrip("\n").split(","))
        for line in lines:
            data_dict[line[0]] = data_dict.get(line[0], 0) + int(line[1])
    with open(report_file_name, "w") as report:
        report.write(f"supply,{data_dict["supply"]}\n")
        report.write(f"buy,{data_dict["buy"]}\n")
        report.write(f"result,{data_dict["supply"] - data_dict["buy"]}\n")
