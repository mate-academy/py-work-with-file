
def create_report(
        data_file_name: str,
        report_file_name: str,
) -> None:
    with open(data_file_name, "r") as f:
        supply_total = 0
        buy_total = 0
        for line in f:
            line = line.strip()
            if not line:
                continue
            op, amount = line.split(",")
            op = op.strip()
            amount = int(amount.strip())
            if op == "supply":
                supply_total += amount
            elif op == "buy":
                buy_total += amount
        result = supply_total - buy_total
    with open(report_file_name, "w") as out:
        out.write(f"supply,{supply_total}\n")
        out.write(f"buy,{buy_total}\n")
        out.write(f"result,{result}\n")
