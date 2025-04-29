def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            transaction_type, amount_text = line.split(",")
            amount = int(amount_text)
            if transaction_type == "supply":
                supply_total += amount
            elif transaction_type == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{supply_total}\n")
        output_file.write(f"buy,{buy_total}\n")
        output_file.write(f"result,{result}\n")