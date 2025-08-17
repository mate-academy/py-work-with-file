def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            operation, amount_str = line.split(",")
            amount = int(amount_str)

            if operation == "supply":
                totals["supply"] += amount
            elif operation == "buy":
                totals["buy"] += amount

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, "w") as out:
        out.write(f"supply,{totals['supply']}\n")
        out.write(f"buy,{totals['buy']}\n")
        out.write(f"result,{result}\n")
