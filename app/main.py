def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    input_file = open(data_file_name, "r")
    for line in input_file:
        line = line.strip()
        if not line:
            continue

        operation, amount = line.split(",")
        amount = int(amount)

        if operation == "supply":
            supply_total += amount
        elif operation == "buy":
            buy_total += amount

    input_file.close()

    result = supply_total - buy_total

    output_file = open(report_file_name, "w")
    output_file.write(f"supply,{supply_total}\n")
    output_file.write(f"buy,{buy_total}\n")
    output_file.write(f"result,{result}\n")

    output_file.close()
