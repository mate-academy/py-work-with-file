def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as data_file:

        supply_count = 0
        buy_count = 0

        data = data_file.readlines()

        for row in data:
            line = row.split(",")
            operation = line[0]
            amount = line[1]

            if operation == "supply":
                supply_count += int(amount)
            elif operation == "buy":
                buy_count += int(amount)

        with open(report_file_name, "w") as result_file:

            result = supply_count - buy_count

            result_file.write(
                f"supply,{supply_count}\n"
                f"buy,{buy_count}\n"
                f"result,{result}\n"
            )
