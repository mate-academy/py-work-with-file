def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        result = []
        total_supply = 0
        total_buy = 0

        for line in data_file:
            if line.strip() == "":
                continue
            result = line.split(",")
            operation = result[0]
            amount = int(result[1])

            if operation == "supply":
                total_supply += amount

            if operation == "buy":
                total_buy += amount

        result = total_supply - total_buy

        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{total_supply}\n"
                              f"buy,{total_buy}\n"
                              f"result,{result}\n")
