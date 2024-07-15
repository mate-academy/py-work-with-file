def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_total = 0
    supply_total = 0
    with open(data_file_name, "r") as f:
        for line in f:
            action, value = line.split(",")
            if action == "supply":
                supply_total += int(value)

            if action == "buy":
                buy_total += int(value)

    with open(report_file_name, "w") as f:
        f.write(f"supply, {supply_total}\n")
        f.write(f"buy, {buy_total}\n")
        f.write(f"result, {supply_total - buy_total}\n")
