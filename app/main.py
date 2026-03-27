def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue

            operation, amount = line.split(",")
            amount = int(amount)
            result_dict[operation] = result_dict.get(operation, 0) + amount
    result = result_dict["supply"] - result_dict["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write(f'supply,{result_dict["supply"]}\n')
        report_file.write(f'buy,{result_dict["buy"]}\n')
        report_file.write(f"result,{result}\n")
