def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {}

    with open(data_file_name, "r") as f:
        for line in f:
            key, value = line.split(",")
            value = int(value.strip())

            if key not in totals:
                totals[key] = value
            else:
                totals[key] += value

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, "w") as f:
        f.write(f"supply,{totals['supply']}\n")
        f.write(f"buy,{totals['buy']}\n")
        f.write(f"result,{result}\n")
