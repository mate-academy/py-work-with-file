def create_report(data_file_name: str, report_file_name: str) -> None:
    read_file = open(data_file_name, "r")
    write_file = open(report_file_name, "w")

    supply_total = 0
    buy_total = 0
    for line in read_file.readlines():
        line = line.strip()
        if not line:
            continue

        operation, amount = line.split(",")
        if operation == "supply":
            supply_total += int(amount)
        if operation == "buy":
            buy_total += int(amount)

    write_file.write(f"supply,{supply_total}\n")
    write_file.write(f"buy,{buy_total}\n")
    write_file.write(f"result,{supply_total - buy_total}\n")

    read_file.close()
    write_file.close()
