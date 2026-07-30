def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file:
        supply = 0
        buy = 0
        for line in data_file:
            split_data = (line.rsplit(","))
            if split_data[0] == "supply":
                supply += int(split_data[1])
            if split_data[0] == "buy":
                buy += int(split_data[1])

        result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.write("supply" + "," + str(supply) + "\n")
        report_file.write("buy" + "," + str(buy) + "\n")
        report_file.write("result" + "," + str(result) + "\n")
