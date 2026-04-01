def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0

    with open(data_file_name, "r") as data_file:
        lines = data_file.readlines()

    for line in lines:
        if line.startswith("buy,"):
            buy_sum += int(line[line.index(",") + 1:])
        elif line.startswith("supply,"):
            supply_sum += int(line[line.index(",") + 1:])

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply_sum}\n"
            f"buy,{buy_sum}\n"
            f"result,{supply_sum - buy_sum}\n"
        )
