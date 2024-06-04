def create_report(data_file_name: str, report_file_name: str) -> None:
    supplies_amount = 0
    buy_amount = 0
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        lines = data_file.readlines()
        for line in lines:
            operation, value = line.split(",")
            value = int(value)
            if operation == "supply":
                supplies_amount += value
            elif operation == "buy":
                buy_amount += value
        result = supplies_amount - buy_amount

        report_file.writelines(
            [
                f"supply,{supplies_amount}",
                f"buy, {buy_amount}",
                f"result, {result}"
            ]
        )
