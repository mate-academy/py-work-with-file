def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {}

    with open(data_file_name, "r") as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            operation, amount = line.split(",")
            amount = int(amount)

            if operation not in totals:
                totals[operation] = 0

            totals[operation] += amount

    supply = totals.get("supply", 0)
    buy = totals.get("buy", 0)
    result = supply - buy

    with open(report_file_name, "w") as outfile:
        outfile.write(f"supply,{supply}\n")
        outfile.write(f"buy,{buy}\n")
        outfile.write(f"result,{result}\n")
