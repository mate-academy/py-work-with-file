def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()

            parts = line.split(",")

            operation, amount = parts[0], parts[1]

            if operation == "supply":
                supply_total += int(amount)
            elif operation == "buy":
                buy_total += int(amount)

    result = supply_total - buy_total

    # with open(report_file_name, "w", newline="") as report_file:
    #     report_writer = report_file.write
    #     report_writer(f"supply,{supply_total}\n")
    #     report_writer(f"buy,{buy_total}\n")
    #     report_writer(f"result,{result}\n")
    with open(report_file_name, "w", newline="") as report_file:
        report_writer = report_file.write
        report_writer(f"supply,{supply_total}\n")  # noqa: E231
        report_writer(f"buy,{buy_total}\n")  # noqa: E231
        report_writer(f"result,{result}\n")  # noqa: E231
