def create_report(data_file_name: str, report_file_name: str) -> None:

    operations = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data:
        for line in data:
            if line.strip():
                operation, amount = line.strip().split(",")
                amount = int(amount)
                if operation in operations:
                    operations[operation] += amount

        supply_total = operations["supply"]
        buy_total = operations["buy"]
        result = supply_total - buy_total

        report_result = (
            f"supply,"
            f"{supply_total}"
            f"\nbuy,{buy_total}"
            f"\nresult,{result}\n"
        )

        with open(report_file_name, "w") as report:
            report.write(report_result)
