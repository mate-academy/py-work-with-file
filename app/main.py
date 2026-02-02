def create_report(data_file: str, report_file_name: str) -> None:
    file_content = open(data_file)
    report = {}
    for line in file_content:
        position = line.split(",")
        if position[0] in report:
            report[position[0]] += int(position[1])
        else:
            report[position[0]] = int(position[1])
    with open(report_file_name, "w") as file_content:
        file_content.write("supply" + "," + str(report["supply"]) + "\n")
        file_content.write("buy" + "," + str(report["buy"]) + "\n")
    result = report["supply"] - report["buy"]
    with open(report_file_name, "a") as file_content:
        file_content.write("result," + str(result) + "\n")
