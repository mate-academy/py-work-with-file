def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, "r") as file:
        for line in file:
            if not line.strip():
                continue
            result = line.strip().split(",")
            if result[0] == "supply":
                supply_total += int(result[1])
            elif result[0] == "buy":
                buy_total += int(result[1])
    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{supply_total - buy_total}\n")
