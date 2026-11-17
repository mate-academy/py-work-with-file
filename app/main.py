def create_report(data_file_name: str, report_file_name: str) -> None:
    file_to_change = open(data_file_name)
    lines = file_to_change.readlines()
    file_to_change.close()

    supply_total = 0
    buy_total = 0
    for line in lines:
        line = line.rstrip()
        if not line:
            continue
        operation, amount = line.split(",")
        amount = int(amount)
        if operation == "supply":
            supply_total += amount
        elif operation == "buy":
            buy_total += amount

    result = supply_total - buy_total

    report = (
        f"supply,{supply_total}\n"
        f"buy,{buy_total}\n"
        f"result,{result}\n"
    )

    with open(report_file_name, "w") as file:
        file.write(report)
