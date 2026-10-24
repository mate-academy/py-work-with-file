def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        supply_total = 0
        buy_total = 0
        for line in data_file:
            line = line.strip()
            key, value = line.split(",")
            if key == "supply":
                supply_total += int(value)
            if key == "buy":
                buy_total += int(value)
        result = supply_total - buy_total
        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{supply_total}\n"
                              f"buy,{buy_total}\n"
                              f"result,{result}\n")
