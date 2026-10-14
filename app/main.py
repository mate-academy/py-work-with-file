def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        result_supply = []
        result_buy = []
        for line in data_file:
            if line.strip():
                result = line.split(",")

                if result[0] == "supply":
                    result_supply.append(int(result[1].strip()))
                elif result[0] == "buy":
                    result_buy.append(int(result[1].strip()))
        supply_sum = sum(result_supply)
        buy_sum = sum(result_buy)
        result_supply_buy = supply_sum - buy_sum

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_sum}\n")
        report_file.write(f"buy,{buy_sum}\n")
        report_file.write(f"result,{result_supply_buy}\n")
