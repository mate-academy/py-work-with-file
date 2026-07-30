def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line_split = line.split(",")
            if line_split[0] == "supply":
                supply += int(line_split[1].strip())
            if line_split[0] == "buy":
                buy += int(line_split[1].strip())

    result = supply - buy

    with open(report_file_name, "a") as file:
        file.write("supply" + "," + str(supply) + "\n")
        file.write("buy" + "," + str(buy) + "\n")
        file.write("result" + "," + str(result) + "\n")
