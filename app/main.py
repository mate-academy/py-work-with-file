def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as file_in, \
         open(report_file_name, "w") as file_out:
        lst = file_in.readlines()
        total_supply = 0
        total_buy = 0
        for el in lst:
            if el.startswith("supply"):
                total_supply += int(el.strip("supply,"))
            if el.startswith("buy"):
                total_buy += int(el.strip("buy,"))

        result = total_supply - total_buy
        file_out.writelines(f"supply,{total_supply}\n"
                            f"buy,{total_buy}\nresult,{result}\n")
