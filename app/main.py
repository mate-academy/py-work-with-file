def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_total = 0
    supply_total = 0

    buy_values = []
    supply_values = []

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            parts = line.strip().split(",")
            if (len(parts) == 2
                    and parts[0] in ("buy", "supply")
                    and parts[1].isdigit()):

                value = int(parts[1])
                if parts[0] == "buy":
                    buy_values.append(value)
                    buy_total += value
                else:
                    supply_values.append(value)
                    supply_total += value

    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(supply_total) + "\n")
        report_file.write("buy," + str(buy_total) + "\n")
        report_file.write("result," + str(supply_total - buy_total) + "\n")
