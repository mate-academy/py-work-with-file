def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_amount = 0
    buy_amount = 0

    with open(data_file_name, "r") as f:
        for line in f:
            line.strip()
            if line == "":
                continue
            op, amount = line.split(",")

            if op == "supply":
                supply_amount += int(amount)
            elif op == "buy":
                buy_amount += int(amount)

    result = supply_amount - buy_amount

    with open(report_file_name, "w") as a:
        a.write(f"supply,{supply_amount}\n")
        a.write(f"buy,{buy_amount}\n")
        a.write(f"result,{result}\n")
