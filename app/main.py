def create_report(data_file_name: str, report_file_name: str) -> None:
    open_data_file = open(data_file_name)
    supply_sum = 0
    buy_sum = 0

    for line in open_data_file:
        line = line.strip()
        if not line:
            continue
        operator, numbers = line.split(',')
        numbers = int(numbers)
        if operator == "supply":
            supply_sum += numbers
        elif operator == "buy":
            buy_sum += numbers

    new_numbers = open(report_file_name, "w")
    new_numbers.write(f"supply,{supply_sum}\n")
    new_numbers.write(f"buy,{buy_sum}\n")
    new_numbers.write(f"result,{supply_sum - buy_sum}\n")


