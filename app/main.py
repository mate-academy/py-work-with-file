def create_report(data_file_name: str, report_file_name: str) -> None:
    sum_supply = 0
    sum_buy = 0

    with open(data_file_name, "r") as table, \
            open(report_file_name, "a") as res:
        for line in table:
            data = line.strip().split(",")
            operation, price = data
            if operation == "supply":
                sum_supply += int(price)
            elif operation == "buy":
                sum_buy += int(price)

            result = sum_supply - sum_buy
        res.write(f"supply,{sum_supply}\n")
        res.write(f"buy,{sum_buy}\n")
        res.write(f"result,{result}\n")
