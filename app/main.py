def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_result = 0
    buy_result = 0

    with open(data_file_name, "r") as file:
        for line in file:
            comma_index = line.find(",")
            if line[:comma_index] == "supply":
                supply_result += int(line[comma_index + 1:])
            elif line[:comma_index] == "buy":
                buy_result += int(line[comma_index + 1:])

    with open(report_file_name, "w") as file:
        file.write("supply," + str(supply_result) + "\n")
        file.write("buy," + str(buy_result) + "\n")
        file.write("result," + str(supply_result - buy_result) + "\n")
