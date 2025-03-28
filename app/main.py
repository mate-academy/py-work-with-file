def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as f:
        for line in f:
            fields = line.strip().split(",")
            if fields:
                if fields[0] == "supply":
                    supply_total += int(fields[1])
                elif fields[0] == "buy":
                    buy_total += int(fields[1])

    result = supply_total - buy_total

    with open(report_file_name, "w") as f:
        f.write("supply," + str(supply_total) + "\n")
        f.write("buy," + str(buy_total) + "\n")
        f.write("result," + str(result) + "\n")
