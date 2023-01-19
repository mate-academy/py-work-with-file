def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as flom_file, \
            open(report_file_name, "a") as repor_file:
        supply = 0
        buy = 0
        for line in flom_file:
            operation, number = line.split(",")
            if operation == "supply":
                supply += int(number)
            if operation == "buy":
                buy += int(number)
        repor_file.write("supply," + str(supply) + "\n")
        repor_file.write("buy," + str(buy) + "\n")
        repor_file.write("result," + str(supply - buy) + "\n")
