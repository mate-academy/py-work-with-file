def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            new_line = line.split(",")
            if line.strip():
                if new_line[0] == "supply":
                    supply += int(new_line[1])
                if new_line[0] == "buy":
                    buy += int(new_line[1])
    with open(report_file_name, "w") as report_file:
        result = supply - buy
        report_file.write("supply," + str(supply) + "\n")
        report_file.write("buy," + str(buy) + "\n")
        report_file.write("result," + str(result) + "\n")
