def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        total = {}
        for line in file:
            line = line.strip()
            if not line:
                continue
            operation, amount_str = line.split(",")
            amount = int(amount_str)
            if operation in total:
                total[operation] = total[operation] + amount
            else:
                total[operation] = amount
    result = total["supply"] - total["buy"]
    with open(report_file_name, "w") as file:
        file.write(f'supply,{total["supply"]}\n')
        file.write(f'buy,{total["buy"]}\n')
        file.write(f"result,{result}\n")
