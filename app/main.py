def create_report(data_file_name: str, report_file_name: str) -> None:

    result_dict = {}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            parts = line.strip().split(",")
            operation = parts[0].strip()
            amount = int(parts[1].strip())
            if operation not in result_dict:
                result_dict[operation] = 0
            result_dict[operation] += amount

    supply_sum = result_dict.get("supply", 0)
    buy_sum = result_dict.get("buy", 0)
    result = supply_sum - buy_sum

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_sum}\n"
                          f"buy,{buy_sum}\n"
                          f"result,{result}\n")
