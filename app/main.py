def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_total = 0
    supply_total = 0

    with open(data_file_name, "r") as file_r:
        for line in file_r:
            oper, value = line.split(",")
            if oper == "buy":
                buy_total += int(value)
            elif oper == "supply":
                supply_total += int(value)

    result = supply_total - buy_total

    with open(report_file_name, "w") as file_w:
        file_w.write(f"supply,{supply_total}\n")
        file_w.write(f"buy,{buy_total}\n")
        file_w.write(f"result,{result}\n")
