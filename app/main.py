def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        supply_items = []
        buy_items = []
        for line in data_file:
            if line.split(",")[0] == "supply":
                supply_items.append(line.split(",")[1])
            else:
                buy_items.append(line.split(",")[1])
        sum_supply = sum(int(x) for x in supply_items)
        sum_buy = sum(int(x) for x in buy_items)
        report_content = (
            f"supply,{sum_supply}\n"
            f"buy,{sum_buy}\n"
            f"result,{sum_supply - sum_buy}\n"
        )
        report_file.write(report_content)
