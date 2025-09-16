def create_report(data_file_name : str, report_file_name : str) -> None:
    total_supply = 0
    total_buy = 0
    file_data = open(data_file_name, "r")
    for line in file_data.readlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        operation = parts[0]
        amount = int(parts[1])

        if operation == "supply":
            total_supply += amount
        elif operation == "buy":
            total_buy += amount
        result = total_supply - total_buy
        file_report = open(report_file_name, "w")
        file_report.write(
            f'supply,{total_supply}\n'
            f'buy,{total_buy}\n'
            f'result,{result}\n')
        file_report.close()
        file_data.close()
