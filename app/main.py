def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as f:
        for line in f:
            row = line.strip().split(",")
            if row[0] == "supply":
                value = int(row[1])
                supply_total += value
            elif row[0] == "buy":
                value = int(row[1])
                buy_total += value

        result = supply_total - buy_total

    with open(report_file_name, "w") as w:
        w.write(f"supply,{str(supply_total)}\n")
        w.write(f"buy,{str(buy_total)}\n")
        w.write(f"result,{str(result)}\n")