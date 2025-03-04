def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as f:
        for line in f:
            line = line.strip().split(",")
            if line[0] == "supply":
                supply += int(line[1])
            if line[0] == "buy":
                buy += int(line[1])
        result = supply - buy

    with open(report_file_name, "w") as new_file:
        new_file.writelines(["supply," + str(supply) +"\n", "buy,"
                             + str(buy) + "\n", "result,"
                             + str(result) + "\n"])
