def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            row = line.strip().split(",")

            if row[0] == "supply":
                total_supply += int(row[1])
            elif row[0] == "buy":
                total_buy += int(row[1])
    result = total_supply - total_buy
    report = [["supply", total_supply], ["buy", total_buy], ["result", result]]

    with open(report_file_name, "w") as report_file:
        for row in report:
            report_file.write(",".join(map(str, row)) + "\n")
