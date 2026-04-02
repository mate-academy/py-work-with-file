def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):

        total_buy = 0
        total_supply = 0

        for line in data_file:
            operation, amount = line.strip().split(",")
            amount = int(amount)

            if operation == "buy":
                total_buy += amount
            elif operation == "supply":
                total_supply += amount

        result = total_supply - total_buy

        report_file.write("supply,%d\n" % total_supply)
        report_file.write("buy,%d\n" % total_buy)
        report_file.write("result,%d\n" % result)
