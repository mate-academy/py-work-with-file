def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_total = 0
    supply_total = 0

    with open(data_file_name, "r") as lines:
        for line in lines:
            name, value = line.strip().split(",")
            value = int(value)
            if name == "supply":
                supply_total += value
            elif name == "buy":
                buy_total += value

    result = supply_total - buy_total

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply_total}\nbuy,{buy_total}\n"
                f"result,{result}\n")
