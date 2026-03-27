def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    read_file = open(data_file_name)
    for line in read_file:
        line = line.strip()
        if not line:
            continue

        operation, amount_str = line.split(",")
        amount = int(amount_str)

        if operation == "supply":
            supply_total += amount
        elif operation == "buy":
            buy_total += amount

    result = supply_total - buy_total

    write_file = open(report_file_name, "w")
    write_file.write(f"supply,{supply_total}\n")
    write_file.write(f"buy,{buy_total}\n")
    write_file.write(f"result,{result}\n")
