def create_report(data_file_name: str, report_file_name: str) -> None:
    report: dict[str, int] = {
        "buy": 0,
        "supply": 0
    }

    with open(data_file_name, "r") as file:
        for line in file.read().split("\n"):
            if line:
                operation, amount = line.split(",")

                if operation == "buy":
                    report["buy"] += int(amount)

                if operation == "supply":
                    report["supply"] += int(amount)

    with open(report_file_name, "w") as file:
        file.write(f'supply,{report["supply"]}\n')
        file.write(f'buy,{report["buy"]}\n')
        file.write(f'result,{report["supply"] - report["buy"]}\n')
