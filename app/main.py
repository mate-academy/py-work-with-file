def create_report(data_file_name: str, report_file_name: str) -> None:

    supply_sum = 0
    buy_sum = 0

    with (
        open(data_file_name, "r") as source,
        open(report_file_name, "w") as report
    ):

        for line in source.readlines():
            item, value = line.strip().split(",")
            if item == "supply":
                supply_sum += int(value)
            if item == "buy":
                buy_sum += int(value)

        result = supply_sum - buy_sum

        report.write(
            f"supply,{supply_sum}\n"
            f"buy,{buy_sum}\n"
            f"result,{result}\n"
        )
