def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):
        supply_amount = 0
        buy_amount = 0
        for line in file_in:
            line = line.split(",")
            if "supply" in line:
                supply_amount += int(line[1])
            else:
                buy_amount += int(line[1])

        result_amount = supply_amount - buy_amount

        file_out.write(f"supply,{supply_amount}\n"
                       f"buy,{buy_amount}\n"
                       f"result,{result_amount}\n")
