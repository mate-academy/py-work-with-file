def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_result = 0
    buy_result = 0

    fle = open(data_file_name, "r")
    reader = fle.readlines()
    fle.close()

    for line in reader:
        line = line.strip()
        if not line:
            continue
        operation, amount = line.split(",")
        amount = int(amount)
        if operation == "supply":
            supply_result += amount
        elif operation == "buy":
            buy_result += amount

    new_file = open(report_file_name, "w")
    new_file.write(f"supply,{supply_result}\n")
    new_file.write(f"buy,{buy_result}\n")
    new_file.write(f"result,{supply_result - buy_result}\n")
    new_file.close()
