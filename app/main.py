def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data,
        open(report_file_name, "w") as report
    ):
        supply = 0
        buy = 0

        for line in data:
            line = line.strip()
            if not line:
                continue
            operation, amount = line.split(",")
            amount = int(amount)

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

        result = supply - buy
        report.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{result}"
        )
