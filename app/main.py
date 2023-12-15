def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        lines = data_file.readlines()

    supply_total = 0
    buy_total = 0

    for line in lines:
        if not line.strip():
            continue

        operation, amount = line.strip().split(",")

        if operation == "supply":
            supply_total += int(amount)
        elif operation == "buy":
            buy_total += int(amount)

    result = supply_total - buy_total

    report = f"supply,{supply_total}\nbuy,{buy_total}\nresult,{result}\n"

    with open(report_file_name, "w") as report_file:
        report_file.write(report)
