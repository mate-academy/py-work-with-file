def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    f1 = open(data_file_name, "r")

    for line in f1:
        if not line.strip():
            continue
        operation, amount = line.strip().split(",")
        amount = int(amount)

        if operation == "buy":
            buy_total += amount
        if operation == "supply":
            supply_total += amount

    f1.close()
    result = supply_total - buy_total
    f2 = open(report_file_name, "w")
    f2.write(f"supply,{supply_total}\n")
    f2.write(f"buy,{buy_total}\n")
    f2.write(f"result,{result}\n")
    f2.close()
