def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {"supply": 0, "buy": 0}

    for line in list(open(data_file_name)):
        if "supply" in line:
            result_dict["supply"] += int(line.strip().split(",")[1])
        if "buy" in line:
            result_dict["buy"] += int(line.strip().split(",")[1])

    supply = result_dict["supply"]
    buy = result_dict["buy"]
    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(supply) + "\n")
        report_file.write("buy," + str(buy) + "\n")
        report_file.write("result," + str(result) + "\n")
