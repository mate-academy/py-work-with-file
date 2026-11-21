def create_report(data_file_name: str, report_file_name: str) -> None:
    counter = {"supply": 0, "buy": 0}

    with open(data_file_name) as lines:
        for line in lines:
            operation, amount = line.split(",")
            amount = int(amount)
            if operation == "supply":
                counter["supply"] += amount
            else:
                counter["buy"] += amount

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{counter['supply']}\n"
            f"buy,{counter['buy']}\n"
            f"result,{counter['supply'] - counter['buy']}\n"
        )
