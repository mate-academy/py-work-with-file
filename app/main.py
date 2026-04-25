def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}
    input_file = open(data_file_name, "r")

    for line in input_file:
        line = line.strip()
        split_line = line.split(",")
        if split_line[0] not in report_dict:
            report_dict[split_line[0]] = int(split_line[1])
        else:
            report_dict[split_line[0]] += int(split_line[1])

    supply = report_dict.get("supply")
    buy = report_dict.get("buy")
    result = supply - buy

    result_file = open(report_file_name, "w")
    result_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
