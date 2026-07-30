def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    input_file = open(data_file_name, "r")
    lines = input_file.readlines()
    input_file.close()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        operation, amount_str = line.split(",")
        amount = int(amount_str)
        if operation == "supply":
            supply_total += amount
        elif operation == "buy":
            buy_total += amount

    result = supply_total - buy_total

    output_file = open(report_file_name, "w")
    output_file.write(f"supply,{supply_total}\n")
    output_file.write(f"buy,{buy_total}\n")
    output_file.write(f"result,{result}\n")
    output_file.close()
