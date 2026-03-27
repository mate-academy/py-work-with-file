def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        lines = file.readlines()
    supply_total = 0
    buy_total = 0
    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        parts = cleaned_line.split(",")
        operation = parts[0]
        value_str = parts[1]
        value = int(value_str)
        if operation == "supply":
            supply_total += value
        else:
            buy_total += value
    result = supply_total - buy_total
    with open(report_file_name, "w") as file_2:
        supply_line = f"supply,{supply_total}\n"
        buy_line = f"buy,{buy_total}\n"
        result_line = f"result,{result}\n"
        file_2.write(supply_line)
        file_2.write(buy_line)
        file_2.write(result_line)
