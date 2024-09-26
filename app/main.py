def create_report(data_file_name: str, report_file_name: str) -> int | str:
    supply_total = 0
    buy_total = 0
    print(data_file_name, report_file_name)
    with open(data_file_name, "r") as file:
        for line in file:
            operator, amount = line.strip().split(",")
            amount = int(amount)
            if operator == "supply":
                supply_total += amount
            elif operator == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f'supply,{supply_total}\n')
        report_file.write(f'buy,{buy_total}\n')
        report_file.write(f'result,{result}\n')

    return result, report_file_name
