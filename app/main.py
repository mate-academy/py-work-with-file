def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as file_data,
        open(report_file_name, "w") as file_report
    ):
        supply = []
        buy = []
        for line in file_data.readlines():
            list_line = line.replace("\n", "").split(",")
            if "supply" in list_line:
                supply.append(int(list_line[1]))
            if "buy" in list_line:
                buy.append(int(list_line[1]))
        sum_supply = sum(supply)
        sum_buy = sum(buy)
        file_report.write(f"supply,{sum_supply}\n")
        file_report.write(f"buy,{sum_buy}\n")
        file_report.write(f"result,{sum_supply - sum_buy}\n")
