def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0, "result" : 0}

    with open(data_file_name, "r") as file:
        for line in file.readlines():
            operation, amount = line.split(",")
            totals[operation] += int(amount)

    totals["result"] = totals["supply"] - totals["buy"]

    with open(report_file_name, "w") as file:
        for key, value in totals.items():
            file.write(f"{key},{value}\n")
