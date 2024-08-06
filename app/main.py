def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as f:
        for line in f:
            line = line.split(",")
            if line[0] == "buy":
                buy += int(line[1])
            else:
                supply += int(line[1])

    with open(report_file_name, "w") as f:
        f.write("supply," + str(supply) + "\n")
        f.write("buy," + str(buy) + "\n")
        f.write("result," + str(supply - buy) + "\n")
