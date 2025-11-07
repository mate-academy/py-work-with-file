def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    csv_file = open(data_file_name, "r")

    supply_sum = 0
    buy_sum = 0
    result = 0

    for row in csv_file:
        row = row.strip()
        op, val = row.split(",", 1)
        if op == "supply":
            supply_sum += int(val)
        if op == "buy":
            buy_sum += int(val)
    result = supply_sum - buy_sum

    csv_file.close()

    csv_file_to_write = open(report_file_name, "a")

    csv_file_to_write.write(f"supply,{supply_sum}\n")
    csv_file_to_write.write(f"buy,{buy_sum}\n")
    csv_file_to_write.write(f"result,{result}\n")

    csv_file_to_write.close()
