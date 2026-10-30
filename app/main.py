def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_total = 0
    supply_total = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            parts = line.split(",")
            if parts[0] == "buy":
                buy_total += int(parts[1])
            elif parts[0] == "supply":
                supply_total += int(parts[1])
    result = supply_total - buy_total
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n"
                          f"buy,{buy_total}\n"
                          f"result,{result}\n")
    # print(f"Buy total: {buy_total}")
    # print(f"Supply total: {supply_total}")
