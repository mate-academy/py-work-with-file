def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file_in:
        for line in file_in:
            operation, amount = line.strip().split(",")
            report[operation] += int(amount)

    result = report["supply"] - report["buy"]

    with open(report_file_name, "w") as file_out:
        file_out.write(f"supply,{report['supply']}\n")
        file_out.write(f"buy,{report['buy']}\n")
        file_out.write(f"result,{result}\n")
