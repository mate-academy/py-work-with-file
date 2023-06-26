def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as data_file, \
         open(report_file_name, "a") as report_file:
        for line in data_file:
            row = line.strip().split(",")

            if row:
                operation_type, amount = row[0], int(row[1])

                if operation_type == "supply":
                    supply_total += amount
                elif operation_type == "buy":
                    buy_total += amount

        result = supply_total - buy_total

        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
