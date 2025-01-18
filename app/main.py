def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as file:
        for line in file:
            if line != "\n":
                operation, value = line.split(",")
                value = int(value)
                if operation == "supply":
                    supply_total += value
                elif operation == "buy":
                    buy_total += value

    result = supply_total - buy_total

    print(
        f"supply_total: {supply_total}, "
        f"buy_total: {buy_total}, result: {result}"
    )

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")
