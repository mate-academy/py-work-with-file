
def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as csv_file:
        lines = csv_file.readlines()

        for line in lines:
            colums = line.strip().split(",")
            print(colums)

            if colums:
                operation_type, amount = colums

                if operation_type == "supply":
                    supply_total += int(amount)
                elif operation_type == "buy":
                    buy_total += int(amount)

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply_total}\n"
            f"buy,{buy_total}\n"
            f"result,{result}\n"
        )
