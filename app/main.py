def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for line in file:
            if not line:
                continue
            line = line.split(",")
            if line[0] == "supply":
                line[1] = int(line[1])
                supply += line[1]
            if line[0] == "buy":
                line[1] = int(line[1])
                buy += line[1]
        result = supply - buy

    with open(report_file_name, "w") as file:
        file.write("supply," + str(supply) + "\n")
        file.write("buy," + str(buy) + "\n")
        file.write("result," + str(result) + "\n")
