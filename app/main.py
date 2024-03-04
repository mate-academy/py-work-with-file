def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as f:
        for line in f:
            operation, amount = line.split(',')
            operations[operation] += int(amount)

    with open(report_file_name, "w") as f:
        f.write(f"supply,{operations['supply']}\n"
                f"buy,{operations['buy']}\n"
                f"result,{operations['supply'] - operations['buy']}\n")
