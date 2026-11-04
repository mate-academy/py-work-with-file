def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:                       # empty string is "falsy"
                continue
            operation, amount = line.split(",")
            totals[operation] += int(amount)   # no if/elif needed

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, "w") as file:
        file.write(f"supply,{totals['supply']}\n")
        file.write(f"buy,{totals['buy']}\n")
        file.write(f"result,{result}\n")
