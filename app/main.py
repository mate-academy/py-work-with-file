def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0
    with open(data_file_name, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            type_, amount_str = line.split(",")
            amount = int(amount_str)
            if type_ == "supply":
                supply_sum += amount
            elif type_ == "buy":
                buy_sum += amount
    with open(report_file_name, "w") as out:
        out.write(f"supply,{supply_sum}\n")
        out.write(f"buy,{buy_sum}\n")
        out.write(f"result,{supply_sum - buy_sum}\n")
