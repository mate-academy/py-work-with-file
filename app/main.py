def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file_in:
        for line in file_in:
            if line == "":
                continue
            line_list = line.split(",")
            if line_list[0] not in report_dict:
                report_dict[line_list[0]] = int(line_list[1])
            else:
                report_dict[line_list[0]] += int(line_list[1])
    result = report_dict["supply"] - report_dict["buy"]
    with open(report_file_name, "w") as file_out:
        for ind, key in report_dict.items():
            file_out.write(f"{ind},{key}\n")
        file_out.write(f"result,{result}\n")
