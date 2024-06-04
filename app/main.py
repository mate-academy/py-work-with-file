def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0

    with open(data_file_name, mode="r", newline="") as file:
        for line in file:
            file_info = line.strip().split(",")
            if file_info[0] == "supply":
                supply_sum += int(file_info[1])
            elif file_info[0] == "buy":
                buy_sum += int(file_info[1])

    with open(report_file_name, mode="w", newline="") as file:
        file.write(
            f"supply, {supply_sum}\n"
            f"buy, {buy_sum}\n"
            f"result, {supply_sum - buy_sum}\n"
            .replace(" ", "")
        )
