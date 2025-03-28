def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0
    with (
        open(f"{data_file_name}", "r") as file,
        open(f"{report_file_name}", "w") as report_file
    ):
        result_list = [
            {pair.split(",")[0]: pair.split(",")[1]}
            for pair in [line.strip() for line in file]
        ]
        for dict_data in result_list:
            if dict_data.get("supply"):
                supply_sum += int(dict_data.get("supply"))
            if dict_data.get("buy"):
                buy_sum += int(dict_data.get("buy"))
        result = supply_sum - buy_sum
        report_file.write(
            f"supply,{supply_sum}\n"
            f"buy,{buy_sum}\n"
            f"result,{result}\n"
        )
