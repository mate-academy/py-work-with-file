def create_report(data_file_name: str,
                  report_file_name: str
                  ) -> None:
    total_supply = 0
    total_buy = 0
    result = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            split_line = line.split(",")
            operation = split_line[0].strip()
            amount = int(split_line[1].strip())
            if operation == "buy":
                total_buy += amount
            elif operation == "supply":
                total_supply += amount
        result = total_supply - total_buy
    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(total_supply) + "\n"
                          + "buy," + str(total_buy) + "\n"
                          + "result," + str(result) + "\n")
