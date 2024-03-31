def create_report(data_file_name: str, report_file_name: str) -> None:
    sum_supply = 0
    sum_buy = 0
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            parts = line.split(",")
            if parts[0] == "supply":
                sum_supply += int(parts[1])
            if parts[0] == "buy":
                sum_buy += int(parts[1])

    result = sum_supply - sum_buy

    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(sum_supply) + "\n")
        report_file.write("buy," + str(sum_buy) + "\n")
        report_file.write("result," + str(result) + "\n")
