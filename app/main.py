def create_report(data_file_name: str, report_file_name: str) -> None:

    supply_rate = 0
    buy_rate = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if not line:
                break

            value = int(line.split(",")[1])
            if line.startswith("supply"):
                supply_rate += value
            if line.startswith("buy"):
                buy_rate += value

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_rate}\n")
        report_file.write(f"buy,{buy_rate}\n")
        report_file.write(f"result,{supply_rate - buy_rate}\n")
