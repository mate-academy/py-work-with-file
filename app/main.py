def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    data_file = open(data_file_name, "r")

    for line in data_file:
        operation, amount = line.split(",")
        amount = int(amount)
        if operation == "supply":
            supply_total += amount
        if operation == "buy":
            buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")
