def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as input_file:
        for row in input_file:
            parts = row.strip().split(",")
            if parts[0] == "supply":
                value = int(parts[1])
                supply_total += value
            elif parts[0] == "buy":
                value = int(parts[1])
                buy_total += value
        result = supply_total - buy_total

    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{str(supply_total)}\n")
        output_file.write(f"buy,{str(buy_total)}\n")
        output_file.write(f"result,{str(result)}\n")
