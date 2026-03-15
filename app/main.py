def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    result_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            divided_line = line.split(",")
            if "supply" in line:
                result_dict["supply"] += int(divided_line[1])
            elif "buy" in line:
                result_dict["buy"] += int(divided_line[1])
    result = result_dict["supply"] - result_dict["buy"]
    with open(report_file_name, "a") as report_file:
        report_file.write("supply," + str(result_dict["supply"]) + "\n")
        report_file.write("buy," + str(result_dict["buy"]) + "\n")
        report_file.write("result," + str(result) + "\n")
